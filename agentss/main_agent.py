# from agents import Agent, handoff, RunConfig

# from agentss.career_agent import CareerAgent
# from agentss.skill_agent import SkillAgent
# from agentss.job_agent import JobAgent

# CareerMentorAgent = Agent(
#     name="CareerMentorAgent",
#     instructions="You're the main guide. Ask about student's interests and then route to career, skill, or job agents accordingly.",
#     handoffs=[
#         handoff(CareerAgent, on_handoff=lambda ctx: print("🔄 Handing off to CareerAgent")),
#         handoff(SkillAgent, on_handoff=lambda ctx: print("🔄 Handing off to SkillAgent")),
#         handoff(JobAgent, on_handoff=lambda ctx: print("🔄 Handing off to JobAgent")),
#     ]
# )

from agents import Agent, handoff, RunConfig  # Core classes/functions from agents SDK

from agentss.career_agent import CareerAgent  # Import CareerAgent (handles career-related queries)
from agentss.skill_agent import SkillAgent    # Import SkillAgent (handles skill roadmap queries)
from agentss.job_agent import JobAgent        # Import JobAgent (handles job role queries)

# Define the main agent that guides the conversation and routes requests to other agents
CareerMentorAgent = Agent(
    name="CareerMentorAgent",  # Name of this main guiding agent
    instructions="You're the main guide. Ask about student's interests and then route to career, skill, or job agents accordingly.",
    handoffs=[
        # Setup handoffs: if the main agent decides, it forwards the conversation to these agents
        handoff(CareerAgent, on_handoff=lambda ctx: print("🔄 Handing off to CareerAgent")),
        handoff(SkillAgent, on_handoff=lambda ctx: print("🔄 Handing off to SkillAgent")),
        handoff(JobAgent, on_handoff=lambda ctx: print("🔄 Handing off to JobAgent")),
    ]
)
