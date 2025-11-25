import sys
import json
import os
import asyncio
from pydantic import BaseModel, Field

# Google ADK & GenAI Imports
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

# --- 1. SETUP API KEY ---
# Ensure your key is set. You can set this in your terminal or uncomment the line below:
os.environ["GOOGLE_API_KEY"] = "AIzaSyDN1UfMJJUgkQfsASr4Ee2JMMDr2dGfuTY"

if not os.environ.get("GOOGLE_API_KEY"):
    print("Error: GOOGLE_API_KEY environment variable not set.")
    print("Please set it via: $env:GOOGLE_API_KEY='...' (PowerShell) or export GOOGLE_API_KEY='...' (Bash)")
    sys.exit(1)

# --- 2. DEFINE OUTPUT SCHEMA ---
class EmailContent(BaseModel):
    Subject: str = Field(description="The Subject of the Email. Concise and descriptive.")
    Body: str = Field(description="The body of the Email. Well formatted with greetings/signature.")

# --- 3. INITIALIZE AGENT ---
root_agent = LlmAgent(
    name="email_agent",
    # If you don't have access to the 2.5 preview yet, change this to "gemini-1.5-flash"
    model="gemini-2.5-flash", 
    instruction="""
    You are an Email Generation Assistant. Your task is to generate a complete, concise, and professional email based on the user's request.
    The email must include a Subject and a Body that has a professional greeting, clear content, an appropriate closing, and your name as the signature.
    """,
    # This enforces the structure
    output_schema=EmailContent,
    # CRITICAL: This tells ADK to save the result in session.state['email']
    output_key="email", 
)

async def main():
    # --- 4. SESSION SETUP ---
    session_service = InMemorySessionService()
    session_id = "session_001"
    user_id = "user_123"
    app_name = "email_app" 
    
    # Create the session context
    await session_service.create_session(
        session_id=session_id,
        user_id=user_id,
        app_name=app_name
    )

    # --- 5. RUNNER SETUP ---
    # FIX: We MUST provide 'app_name' here so the runner knows which session scope to use
    runner = Runner(
        agent=root_agent, 
        session_service=session_service, 
        app_name=app_name
    )

    # --- 6. RUN AGENT ---
    user_input = "Write a cold email to a potential client offering web design services."
    print(f"User Input: {user_input}")
    print("Processing... (The agent is generating structured data into memory)\n")

    # We run the loop to let the agent process the request.
    # Note: We likely won't see the text *here* because it's being redirected to 'state'.
    async for event in runner.run_async(
        session_id=session_id,
        user_id=user_id,
        new_message=types.Content(parts=[types.Part(text=user_input)])
    ):
        # Optional: Print a dot for every event just to show activity
        print(".", end="", flush=True)

    print("\n\n--- Agent Execution Finished ---")

    # --- 7. RETRIEVE RESULT (The Critical Fix) ---
    # Since we used output_key="email", the agent didn't "speak" the answer; 
    # it saved it to the session's memory state. We must fetch it now.
    
    # FIX: Use keyword arguments here to avoid TypeError
    current_session = await session_service.get_session(
        session_id=session_id, 
        user_id=user_id,
        app_name=app_name
    )
    
    if current_session and current_session.state and "email" in current_session.state:
        # The data is already a dictionary (or object) thanks to ADK parsing it for you
        email_data = current_session.state["email"]
        
        print("\n>>> EMAIL GENERATED SUCCESSFULLY! <<<\n")
        
        # Handle cases where it might be a dict or a Pydantic object depending on SDK version
        subject = email_data.get('Subject') if isinstance(email_data, dict) else email_data.Subject
        body = email_data.get('Body') if isinstance(email_data, dict) else email_data.Body
        
        print(f"Subject: {subject}")
        print("-" * 50)
        print(f"Body:\n{body}")
        print("-" * 50)
    else:
        print("\nError: No email found in session state.")
        print("Raw State Dump:", current_session.state if current_session else "No Session Found")

if __name__ == "__main__":
    asyncio.run(main())