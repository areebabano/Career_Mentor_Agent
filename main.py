import streamlit as st
import asyncio
import os
import json
from datetime import datetime
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from openai.types.responses import ResponseTextDeltaEvent

# Load environment variables (GEMINI_API_KEY)
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("❌ GEMINI_API_KEY missing in .env")

# Setup client & agent
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
set_tracing_disabled(disabled=True)

agent = Agent(
    name="Career Mentor",
    instructions=(
        "You are a professional and friendly career mentor. "
        "Provide advice, quizzes, roadmaps, interview tips, resources, and scheduling help related only to careers. "
        "If the user asks anything unrelated, politely remind them that you are a career mentor and "
        "ask them to please ask career-related questions."
    ),
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
)

def make_prompt(user_input: str, category: str) -> str:
    templates = {
        "Career Advice": f"User says: '{user_input}'. Provide detailed career advice with steps and skills.",
        "Skill Assessment Quiz": f"User interested in '{user_input}'. Create a short 3-question quiz.",
        "Career Roadmap": f"User wants to become '{user_input}'. Give detailed career roadmap.",
        "Resume & Interview Tips": f"User preparing for '{user_input}' job. Give resume tips & 5 common interview Q&A.",
        "Resources & Scheduling": f"User asks: '{user_input}'. Share courses, articles, videos, and help schedule reminders or tasks.",
        "General Conversation": (
            f"User says: '{user_input}'. Politely remind them you are a career mentor and can only answer career-related questions. "
            "If the question is career-related, answer it thoroughly."
        )
    }
    return templates.get(category, templates["Career Advice"])

def save_progress(query, category, response):
    file = "user_progress.json"
    entry = {
        "query": query,
        "category": category,
        "response_summary": response[:150],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    try:
        with open(file, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"history": []}
    data["history"].append(entry)
    with open(file, "w") as f:
        json.dump(data, f, indent=2)

# Initialize session states
if "history" not in st.session_state:
    st.session_state.history = []
if "is_processing" not in st.session_state:
    st.session_state.is_processing = False
if "chat_cleared" not in st.session_state:
    st.session_state.chat_cleared = False

# Streamlit config
st.set_page_config(page_title="Career Mentor Agent", layout="wide")

# Sidebar UI
with st.sidebar:
    st.markdown("""
    <div style='text-align:center;'>
        <img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGxzanAyeTRub3prcDI0cTQ0dDR3bnQydHVoYmFpNGo3MTRqMzJ0ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/58OujxlE7e19Mjv0gj/giphy.gif' width='180'/>
        <h1 style='margin-top:5px;'>🎓 Career Mentor Agent</h1>
        <p style='font-size:13px;color:gray;'>AI powered career guidance with quizzes, tips, resources & reminders</p>
    </div>""", unsafe_allow_html=True)

    st.markdown("---")
    category = st.selectbox("Select Help Type:", [
        "General Conversation",
        "Career Advice",
        "Skill Assessment Quiz",
        "Career Roadmap",
        "Resume & Interview Tips",
        "Resources & Scheduling"
    ])
    st.markdown("---")

    st.subheader("📋 Feedback")
    rating = st.slider("Rate your session:", 1, 5, 3)
    comment = st.text_area("Your feedback (optional)")
    if st.button("Submit Feedback"):
        st.success("🎉 Thanks for your feedback!")
        # Optional: Save feedback to file or DB

    st.markdown("---")
    if st.button("Clear Chat"):
        st.session_state.history = []
        st.session_state.chat_cleared = True

# Show message to refresh after clearing chat
if st.session_state.chat_cleared:
    st.info("Chat cleared! Please refresh the page (F5) to reset completely.")
    st.stop()

# Main Chat UI
st.title("🎓 Career Mentor Agent 🌠")

# Show chat history
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box disabled during processing
user_input = st.chat_input(
    "Type your career goal or question here...",
    disabled=st.session_state.is_processing
)

if user_input and not st.session_state.is_processing:
    st.session_state.history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        st.session_state.is_processing = True

        async def stream_response():
            try:
                full_response = ""
                prompt = make_prompt(user_input, category)
                stream = Runner.run_streamed(agent, prompt)

                async for event in stream.stream_events():
                    if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                        full_response += event.data.delta
                        placeholder.markdown(full_response + "▌")

                placeholder.markdown(full_response)
                st.session_state.history.append({"role": "assistant", "content": full_response})
                save_progress(user_input, category, full_response)

            except Exception as e:
                st.error(f"❗❌ Error: {str(e)}")
            finally:
                st.session_state.is_processing = False

        asyncio.run(stream_response())