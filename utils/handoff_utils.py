import chainlit as cl
from agents import Agent
from agents import RunContextWrapper

async def notify_handoff(agent: Agent, ctx: RunContextWrapper[None]):
    """
    Send a notification message to Chainlit UI about the handoff event,
    and update the user session with the new agent.
    """
    await cl.Message(
        content=f"🔄 Switching to *{agent.name}*"
    ).send()

    cl.user_session.set("agent", agent)


def handoff_notifier(agent: Agent):
    """
    Returns an async callback function that Chainlit can call
    on agent handoff events.
    """
    async def _on_handoff(ctx: RunContextWrapper[None]):
        await notify_handoff(agent, ctx)

    return _on_handoff
