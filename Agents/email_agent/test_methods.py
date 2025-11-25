# test_methods.py
from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

class Email_content(BaseModel):
    Subject: str
    Body: str

agent = LlmAgent(
    name="test",
    model="gemini-2.0-flash",
    instruction="Generate email",
    output_schema=Email_content,
    output_key="email",
)

# Try different methods
print("Agent methods:", dir(agent))
print("\nTrying to find the right method...")

# Common method names in ADK
methods_to_try = ['generate', '__call__', 'execute', 'invoke', 'query']

for method_name in methods_to_try:
    if hasattr(agent, method_name):
        print(f"✅ Agent has method: {method_name}")