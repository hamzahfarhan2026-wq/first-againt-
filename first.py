import os
from dotenv import load_dotenv

load_dotenv()

from agno.agent import Agent
from agno.models.groq import Groq

agent_v0 = Agent(
    name="agent_v0",
    model=Groq(
        id="openai/gpt-oss-120b",
        api_key=os.getenv("GROQ_API_KEY")
    ),
    instructions="You are a helpful assistant.",
    description="This is a simple agent that can answer questions and provide information.",
    markdown=True
)

agent_v0.print_response("how are you ")
