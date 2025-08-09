import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, function_tool

# --------------------------
# 1. Load Environment Variables
# --------------------------
# load_dotenv() will read your .env file and add variables (like GEMINI_API_KEY) to your environment
load_dotenv()

# --------------------------
# 2. Initialize Gemini API Client (OpenAI-Compatible)
# --------------------------
# AsyncOpenAI is a wrapper that works like OpenAI's SDK but can connect to other API endpoints (like Gemini)
# base_url points to Google's Gemini API OpenAI-compatible endpoint
external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),  
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# --------------------------
# 3. Define the Tool Function
# --------------------------
# @function_tool decorator makes this function usable as a "tool" in an Agent-based system.
# It can be called directly by another Agent (e.g., SkillAgent).
@function_tool
async def get_career_roadmap(career_field: str):
    print(f"🔧 Tool get_career_roadmap called with: {career_field}")
    """
    Generates a detailed skill roadmap for a given career field.

    Args:
        career_field (str): The career or skill area for which to generate the roadmap.

    Returns:
        dict: A structured skill roadmap with beginner, intermediate, and advanced stages.
    """
    try:
        # --------------------------
        # 4. Input Validation
        # --------------------------
        # Ensure the career_field is a valid non-empty string
        if not career_field or not isinstance(career_field, str) or not career_field.strip():
            return {
                "error": "⚠ Please provide a valid career field name (e.g., 'Data Scientist', 'Web Developer')."
            }

        # --------------------------
        # 5. Prompt Engineering
        # --------------------------
        # This is the instruction we send to the AI model.
        # It clearly explains the required output structure and details.
        prompt = f"""
You are an expert career mentor and skill development planner.

The student is interested in becoming a **{career_field}**.

Please create a **comprehensive skill development roadmap** that includes:
- **Beginner Level**: Foundational skills and concepts to start with.
- **Intermediate Level**: Skills, tools, and projects to advance to the next stage.
- **Advanced Level**: High-level, specialized, or expert skills for mastery.
- Recommended **learning resources** (online courses, books, or tools) for each level.
- **Practical projects** to build a portfolio.
- **Estimated time** required for each stage (in months).
- **Tips for success** and common mistakes to avoid.

**Output Format:**
Organize the answer with clear headings and bullet points.
Number each step clearly.
Keep it concise but actionable.
        """

        # --------------------------
        # 6. API Call to Gemini (OpenAI-Compatible Mode)
        # --------------------------
        # Sends the prompt to Gemini's chat completion API and waits for the response
        response = await external_client.chat.completions.create(
            model="gemini-2.0-flash",               # Model to use
            messages=[{"role": "user", "content": prompt}],  # Chat history with our prompt
            temperature=0.7,                        # Creativity level (0 = more strict, 1 = more creative)
            max_tokens=1000                         # Max length of the output
        )

        # --------------------------
        # 7. Extract Output in One Line (Safe)
        # --------------------------
        # Tries to get message.content from the first choice, defaults to a warning if empty
        # output = (
        #     getattr(response.choices[0].message, "content", None)
        #     or response.choices[0].message.get("content", "")
        #     or "⚠ No roadmap generated."
        # ).strip()
        output = response.choices[0].message.content

        # --------------------------
        # 8. Return Structured Result
        # --------------------------
        # Always return in JSON format so the agent can handle it consistently
        return {
            "career_field": career_field,
            "skill_roadmap": output
        }

    except Exception as e:
        # --------------------------
        # 9. Error Handling
        # --------------------------
        # If something goes wrong, log the error and return it in the response
        error_msg = f"❌ Exception in get_career_roadmap tool: {str(e)}"
        print(error_msg)
        return {"error": error_msg}
