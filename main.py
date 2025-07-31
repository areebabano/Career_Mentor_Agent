# import os
# from dotenv import load_dotenv
# import chainlit as cl
# from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig, set_tracing_disabled
# from agentss.main_agent import CareerMentorAgent

# # Load environment variables
# load_dotenv()
# set_tracing_disabled(True)

# # Initialize API client and model
# external_client = AsyncOpenAI(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# model = OpenAIChatCompletionsModel(
#     model="gemini-2.5-flash",
#     openai_client=external_client,
# )

# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# # Chainlit event: start of chat
# @cl.on_chat_start
# async def start():
#     await cl.Message(content="👋 Welcome! Ask me anything about your career journey.").send()

# # Chainlit event: user sends a message
# @cl.on_message
# async def main(message: cl.Message):
#     user_input = message.content

#     # Run your CareerMentorAgent synchronously with user input
#     result = Runner.run_sync(CareerMentorAgent, user_input, run_config=config)

#     # Send the agent's response back to Chainlit UI
#     await cl.Message(content=result.final_output).send()

# # Optional: Uncomment below if you want to test CLI run directly
# # if __name__ == "__main__":
# #     prompt = "I want to know what career paths are available in data analysis."
# #     result = Runner.run_sync(CareerMentorAgent, prompt, run_config=config)
# #     print("\n🧠 Final Result:\n", result.final_output)


import os
from dotenv import load_dotenv  # Load environment variables from .env file
import chainlit as cl           # Chainlit framework for chat UI
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig, set_tracing_disabled
from agentss.main_agent import CareerMentorAgent  # Your main agent coordinating career guidance

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
    model="gemini-2.5-flash",  # Specify model version
    openai_client=external_client,
)

# Configuration for running the agent, including model and client details
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Chainlit event handler: triggered when chat session starts
@cl.on_chat_start
async def start():
    # Send a welcome message to user in the chat UI
    await cl.Message(content="👋 Welcome! Ask me anything about your career journey.").send()

# Chainlit event handler: triggered when user sends a message
@cl.on_message
async def main(message: cl.Message):
    user_input = message.content  # Extract text content from user message

    # Run the CareerMentorAgent synchronously with user input and config
    result = Runner.run_sync(CareerMentorAgent, user_input, run_config=config)

    # Send the agent's response back to the Chainlit chat interface
    await cl.Message(content=result.final_output).send()

# Optional CLI test block (commented out) to run the agent directly from terminal
# if __name__ == "__main__":
#     prompt = "I want to know what career paths are available in data analysis."
#     result = Runner.run_sync(CareerMentorAgent, prompt, run_config=config)
#     print("\n🧠 Final Result:\n", result.final_output)
