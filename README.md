
🎯 Career Mentor Agent
Welcome to the Career Mentor Agent — your AI-powered career advisor!
It helps you explore career options, discover required skills, and understand potential job roles — all through intelligent conversation.
Built using OpenAI Agents SDK, Gemini API, and Chainlit for a seamless interactive experience. 🚀

✨ Features
🤖 Main Career Mentor Agent — routes queries to the right agent

🧭 Career Agent — suggests career paths based on your interests

🛠️ Skill Agent — provides skill roadmaps for each career

💼 Job Agent — lists job titles related to your chosen field

🧩 Tool Integration — uses a roadmap tool to fetch learning paths

🔀 Automatic Handoff — intelligently switches between agents

💬 Chainlit UI — chat with the mentor in a web interface

⚙️ Getting Started
🔐 Prerequisites
Python 3.8+

Gemini API key from Google Generative Language API

Dependencies in requirements.txt

🛠️ Installation
bash
Copy
Edit
git clone https://github.com/yourusername/career-mentor-agent.git
cd career-mentor-agent
pip install -r requirements.txt
🔑 Environment Setup
Create a .env file:

env
Copy
Edit
GEMINI_API_KEY=your_api_key_here
🖥️ How to Use
💻 Run in Terminal with Chainlit UI
bash
Copy
Edit
chainlit run main.py
Then visit 👉 http://localhost:8000 to chat with your AI career mentor!

🗂️ Project Structure
bash
Copy
Edit
career-mentor-agent/
│
├── agentss/
│   ├── main_agent.py       # 🤖 CareerMentorAgent
│   ├── career_agent.py     # 🧭 CareerAgent
│   ├── skill_agent.py      # 🛠️ SkillAgent
│   ├── job_agent.py        # 💼 JobAgent
│
├── tools/
│   └── roadmap.py          # 📚 Roadmap tool for skills
│
├── main.py                 # 🚀 App entry point
├── .env                    # 🔐 Environment variables
├── requirements.txt        # 📦 Dependencies
└── README.md               # 📄 You’re reading it!
🧠 How It Works
🗣️ User asks a question (e.g. career advice, skills needed, or job roles).

🤖 CareerMentorAgent processes the input and hands off to the appropriate sub-agent.

🔀 Agent Handoff:

"I want to explore careers in AI" → 🧭 CareerAgent

"What skills do I need for data analyst?" → 🛠️ SkillAgent

"What jobs are there in cybersecurity?" → 💼 JobAgent

🧩 SkillAgent uses roadmap tool to fetch learning steps dynamically.

💬 Response is returned to the user in real-time.

💬 Example Conversation
pgsql
Copy
Edit
👤 User: I want to explore a career in data science.
🧭 CareerAgent: Data Science offers paths like Data Scientist, ML Engineer, Analyst, etc.

👤 User: What skills should I learn to become a data analyst?
🛠️ SkillAgent: You should start with Excel, SQL, basic stats, data cleaning, and visualization tools.

👤 User: What are the job roles in cybersecurity?
💼 JobAgent: Security Analyst, Pen Tester, SOC Analyst, and Security Engineer are popular roles.
📄 License
MIT License © 2025 Areeba Hammad
