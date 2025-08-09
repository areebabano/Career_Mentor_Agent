import chainlit as cl
from agents import Runner
from agentss.career_mentor_agent import CareerMentorAgent
from config import config  # Your RunConfig or equivalent config

@cl.on_chat_start
async def start():
    # Initialize conversation history for this user session
    cl.user_session.set("history", [])
    await cl.Message("👋 Welcome! Tell me about your interests or goals, and I’ll help guide your career journey.").send()

@cl.on_message
async def handle(message: cl.Message):
    # Get current conversation history or empty list
    history = cl.user_session.get("history", [])
    
    # Append current user message to history
    history.append({"role": "user", "content": message.content})

    # Show thinking indicator in chat UI
    thinking_msg = await cl.Message("💡Thinking...").send()

    try:
        # Run the CareerMentorAgent with full history as context
        result = await Runner.run(
            CareerMentorAgent,
            history,
            run_config=config
        )
        
        assistant_reply = result.final_output

        # Update thinking message with assistant's response
        thinking_msg.content = assistant_reply
        await thinking_msg.update()

        # Update conversation history with assistant's reply, using agent's helper
        updated_history = result.to_input_list()
        cl.user_session.set("history", updated_history)

    except Exception as e:
        # On error, update thinking message with error info
        thinking_msg.content = f"❌ Error occurred: {e}"
        await thinking_msg.update()
