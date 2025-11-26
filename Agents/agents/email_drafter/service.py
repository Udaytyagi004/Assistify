import os
import sys
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# --- 1. SYSTEM SETUP (CRITICAL FOR MICROSERVICES) ---
# This block ensures we can find the .env file at the ROOT of the project
current_dir = os.path.dirname(os.path.abspath(__file__)) # agents/email_drafter/
root_dir = os.path.abspath(os.path.join(current_dir, "../../")) # ASSISTIFY/
sys.path.append(root_dir) # Add root to python path

from dotenv import load_dotenv
# Explicitly load the .env from the root folder
load_dotenv(os.path.join(root_dir, ".env"))

# --- 2. IMPORTS ---
# Google ADK & GenAI Imports
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

# --- 3. VERIFY KEYS ---
if not os.environ.get("GOOGLE_API_KEY"):
    print("Error: GOOGLE_API_KEY environment variable not set.")
    sys.exit(1)

# --- 4. DEFINE SCHEMAS ---
class UserRequest(BaseModel):
    query: str = Field(..., description="The user's instruction for the email")
    user_id: str = Field("default_user", description="ID of the user")

class EmailContent(BaseModel):
    Subject: str = Field(description="The Subject of the Email")
    Body: str = Field(description="The Body of the Email")

# --- 5. INITIALIZE THE AGENT ---
app = FastAPI(title="Email Drafter API")

root_agent = LlmAgent(
    name="email_drafter_agent", # Renamed for clarity
    model="gemini-2.5-flash",
    instruction="""
    You are an Email Generation Assistant. Generate a professional email based on the user's request.
    The email must include a Subject and a Body.
    """,
    output_schema=EmailContent,
    output_key="email",
)

session_service = InMemorySessionService()
app_name = "email_drafter_service"

# --- 6. ENDPOINT ---
@app.post("/generate-email", response_model=EmailContent)
async def generate_email(request: UserRequest):
    """
    Endpoint to generate an email based on a user prompt.
    """
    session_id = f"session_{request.user_id}"
    
    try:
        await session_service.create_session(
            session_id=session_id,
            user_id=request.user_id,
            app_name=app_name
        )
    except Exception:
        pass

    runner = Runner(
        agent=root_agent, 
        session_service=session_service, 
        app_name=app_name
    )

    async for event in runner.run_async(
        session_id=session_id,
        user_id=request.user_id,
        new_message=types.Content(parts=[types.Part(text=request.query)])
    ):
        pass

    current_session = await session_service.get_session(
        session_id=session_id, 
        user_id=request.user_id, 
        app_name=app_name
    )
    
    if current_session and current_session.state and "email" in current_session.state:
        email_data = current_session.state["email"]
        if isinstance(email_data, dict):
            return EmailContent(**email_data)
        else:
            return email_data
    else:
        raise HTTPException(status_code=500, detail="Agent failed to generate email data")

if __name__ == "__main__":
    # We run on port 8000 for the Drafter
    uvicorn.run(app, host="0.0.0.0", port=8000)