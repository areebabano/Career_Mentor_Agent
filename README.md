🎯 Career Mentor Agent
Welcome to the Career Mentor Agent — your AI-powered career advisor!
It helps you:

✅ Explore career options
✅ Discover required skills
✅ Understand potential job roles

All through intelligent conversation powered by:
🧠 OpenAI Agents SDK · 🪄 Gemini API · 🖥️ Chainlit (for interactive UI)

✨ Features
Feature	Description
🤖 Main Career Mentor Agent	Routes user queries to the right sub-agent
🧭 Career Agent	Suggests career paths based on your interests
🛠️ Skill Agent	Provides skill roadmaps for each career
💼 Job Agent	Lists job titles related to your chosen field
🧩 Tool Integration	Uses a roadmap tool to fetch relevant learning paths
🔀 Automatic Handoff	Intelligently switches between agents
💬 Chainlit UI	Chat with your career mentor in a web interface

⚙️ Getting Started
🔐 Prerequisites
Python 3.8+

Gemini API Key from Google Generative Language API

All required dependencies (listed in requirements.txt)

🛠️ Installation
bash
Copy
Edit
git clone https://github.com/yourusername/career-mentor-agent.git
cd career-mentor-agent
pip install -r requirements.txt
🔑 Environment Setup
Create a .env file in the root directory:

env
Copy
Edit
GEMINI_API_KEY=your_api_key_here
🖥️ How to Use
Run the application in your terminal:

bash
Copy
Edit
chainlit run main.py
Then open your browser and go to 👉 http://localhost:8000
Start chatting with your AI career mentor! 🧑‍🏫✨

🗂️ Project Structure
bash
Copy
Edit
career-mentor-agent/
│
├── agents/
│   ├── main_agent.py       # 🤖 CareerMentorAgent
│   ├── career_agent.py     # 🧭 CareerAgent
│   ├── skill_agent.py      # 🛠️ SkillAgent
│   ├── job_agent.py        # 💼 JobAgent
│
├── tools/
│   └── roadmap.py          # 📚 Skill roadmap fetcher
│
├── main.py                 # 🚀 App entry point
├── .env                    # 🔐 API credentials
├── requirements.txt        # 📦 Python dependencies
└── README.md               # 📄 This file!
🧠 How It Works
🗣️ User asks a question
(e.g., "What jobs are there in AI?", "What skills do I need to be a frontend dev?")

🤖 CareerMentorAgent processes input

🔀 Handoff to relevant sub-agent

"I want to explore careers in AI" → 🧭 CareerAgent

"What skills do I need for data analyst?" → 🛠️ SkillAgent

"What jobs are there in cybersecurity?" → 💼 JobAgent

🧩 SkillAgent uses roadmap tool to fetch learning path

💬 Response is shown in real-time via Chainlit UI

💬 Example Conversation
plaintext
Copy
Edit
👤 User: I want to explore a career in data science.
🧭 CareerAgent: Data Science offers paths like Data Scientist, ML Engineer, Analyst, etc.

👤 User: What skills should I learn to become a data analyst?
🛠️ SkillAgent: You should start with Excel, SQL, basic stats, data cleaning, and visualization tools.

👤 User: What are the job roles in cybersecurity?
💼 JobAgent: Security Analyst, Pen Tester, SOC Analyst, and Security Engineer are popular roles.
📄 License
MIT License © 2025 [Areeba Hammad]
