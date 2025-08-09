import os

from dotenv import load_dotenv  # Load environment variables from .env file

from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig, set_tracing_disabled

# Load environment variables (like API keys)
load_dotenv()

# Disable internal tracing/logging for cleaner output (optional)
set_tracing_disabled(True)

# Initialize the OpenAI-compatible async client with Gemini API key and base URL
external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),  # Fetch API key from environment variables
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Initialize the OpenAI chat model with the async client
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  # Specify model version
    openai_client=external_client,
)

# Configuration for running the agent, including model and client details
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)