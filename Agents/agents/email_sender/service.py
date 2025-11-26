import os
import sys
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# --- 1. SYSTEM SETUP ---
# We need to add the project root to sys.path so we can import 'tools'
current_dir = os.path.dirname(os.path.abspath(__file__)) # agents/email_sender/
root_dir = os.path.abspath(os.path.join(current_dir, "../../")) # ASSISTIFY/
sys.path.append(root_dir) 

from dotenv import load_dotenv
load_dotenv(os.path.join(root_dir, ".env"))

# --- 2. IMPORT THE TOOL ---
from tools.email_tools import send_email_via_smtp

# --- 3. GOOGLE ADK IMPORTS ---
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

if not os.environ.get("GOOGLE_API_KEY"):
    sys.exit("Error: GOOGLE_API_KEY not set.")

# --- 4. DATA SCHEMAS ---

# Input: This is what you (or the frontend) send to this Agent
class EmailDetails(BaseModel):
    Subject: str
    Body: str

class SenderInput(BaseModel):
    recipient_email: str
    email: EmailDetails
    user_id: str = "default_user"

# Output: The Agent reports back if it worked
class SenderOutput(BaseModel):
    status: str = Field(description="Success or Error message from the tool")

# --- 5. INITIALIZE AGENT ---
app = FastAPI(title="Email Sender API")

sender_agent = LlmAgent(
    name="sender_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are an Email Dispatcher.
    1. You will receive a request containing a recipient, subject, and body.
    2. You MUST use the `send_email_via_smtp` tool to deliver the message.
    3. Return the result message from the tool as the status.
    """,
    # HERE IS THE MAGIC: We give the agent the Python function we wrote in Step 1
    tools=[send_email_via_smtp], 
    output_schema=SenderOutput,
    output_key="delivery_result"
)

session_service = InMemorySessionService()
app_name = "email_sender_service"

# --- 6. ENDPOINT ---
@app.post("/dispatch-email", response_model=SenderOutput)
async def dispatch_email(request: SenderInput):
    session_id = f"sender_session_{request.user_id}"

    # Create Session
    try:
        await session_service.create_session(session_id=session_id, user_id=request.user_id, app_name=app_name)
    except:
        pass

    # We format the input as a string for the LLM
    prompt_text = f"""
    Please send this email:
    To: {request.recipient_email}
    Subject: {request.email.Subject}
    Body: {request.email.Body}
    """

    runner = Runner(agent=sender_agent, session_service=session_service, app_name=app_name)

    # Run Agent
    async for event in runner.run_async(
        session_id=session_id, 
        user_id=request.user_id, 
        new_message=types.Content(parts=[types.Part(text=prompt_text)])
    ):
        pass

    # Get Result
    current_session = await session_service.get_session(session_id=session_id, user_id=request.user_id, app_name=app_name)
    
    if current_session and "delivery_result" in current_session.state:
        data = current_session.state["delivery_result"]
        # Handle dict vs object return types
        if isinstance(data, dict):
            return SenderOutput(**data)
        return data
    
    raise HTTPException(status_code=500, detail="Agent failed to dispatch email")

if __name__ == "__main__":
    # IMPORTANT: Run on PORT 8001 (Drafter is on 8000)
    uvicorn.run(app, host="0.0.0.0", port=8001)