from agents import Agent

from tools.roadmap import get_career_roadmap

SkillAgent = Agent(
    name="SkillAgent",
    instructions=(
        "You are a skill advisor. Always answer by using the get_career_roadmap tool. "
        "Do not guess or answer without using the tool."
    ),
    tools=[get_career_roadmap],
)
