import os
import sys
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Google ADK & GenAI Imports
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
os.environ["GOOGLE_API_KEY"] = "AIzaSyDN1UfMJJUgkQfsASr4Ee2JMMDr2dGfuTY"
# --- 1. SETUP API KEY ---
if not os.environ.get("GOOGLE_API_KEY"):
    print("Error: GOOGLE_API_KEY environment variable not set.")
    sys.exit(1)

# --- 2. DEFINE SCHEMAS ---

# This is the structure we expect FROM the user (API Request)
class UserRequest(BaseModel):
    query: str = Field(..., description="The user's instruction for the email")
    user_id: str = Field("default_user", description="ID of the user making the request")

# This is the structure we expect FROM the Agent (Output Schema)
class EmailContent(BaseModel):
    Subject: str = Field(description="The Subject of the Email")
    Body: str = Field(description="The Body of the Email")

# --- 3. INITIALIZE THE APP & AGENT ---
app = FastAPI(title="Email Agent API")

# Initialize Agent (Same as in agent.py)
root_agent = LlmAgent(
    name="email_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are an Email Generation Assistant. Generate a professional email based on the user's request.
    The email must include a Subject and a Body.
    """,
    output_schema=EmailContent,
    output_key="email",
)

# Initialize Session Service (In-memory for this example)
session_service = InMemorySessionService()
app_name = "email_api_service"

# --- 4. DEFINE THE ENDPOINT ---
@app.post("/generate-email", response_model=EmailContent)
async def generate_email(request: UserRequest):
    """
    Endpoint to generate an email based on a user prompt.
    """
    session_id = f"session_{request.user_id}"
    
    # 1. Create or Get Session
    # For a real API, you might want a fresh session per request or retrieve an existing one
    try:
        await session_service.create_session(
            session_id=session_id,
            user_id=request.user_id,
            app_name=app_name
        )
    except Exception:
        # Session likely already exists, which is fine
        pass

    # 2. Setup Runner
    runner = Runner(
        agent=root_agent, 
        session_service=session_service, 
        app_name=app_name
    )

    # 3. Run Agent
    # We don't need to print output here, just process it
    async for event in runner.run_async(
        session_id=session_id,
        user_id=request.user_id,
        new_message=types.Content(parts=[types.Part(text=request.query)])
    ):
        pass # Wait for completion

    # 4. Retrieve Structured Data from Session State
    current_session = await session_service.get_session(
        session_id=session_id, 
        user_id=request.user_id,
        app_name=app_name
    )
    
    if current_session and current_session.state and "email" in current_session.state:
        email_data = current_session.state["email"]
        
        # Convert dictionary to Pydantic model to return strictly typed JSON
        # ADK might store it as a dict or object depending on version
        if isinstance(email_data, dict):
            return EmailContent(**email_data)
        else:
            return email_data
    else:
        raise HTTPException(status_code=500, detail="Agent failed to generate email data")

if __name__ == "__main__":
    # Allows running this file directly: python server.py
    uvicorn.run(app, host="0.0.0.0", port=8000)