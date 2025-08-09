# 🎯 Career Mentor Agent

**Welcome to the Career Mentor Agent — your AI-powered career advisor!**  
This assistant helps you **explore careers**, **discover required skills**, and **understand job roles** — all through intelligent conversations.  
Built with **OpenAI Agents SDK**, **Gemini API**, and **Chainlit** for a seamless interactive experience. 🚀

---

## ✨ Features

- 🤖 **Main Career Mentor Agent** — routes your queries to the correct sub-agent  
- 🧭 **Career Agent** — suggests career paths based on your interests  
- 🛠️ **Skill Agent** — provides skill roadmaps for any chosen career  
- 💼 **Job Agent** — lists job titles related to your selected field  
- 🧩 **Tool Integration** — uses a roadmap tool to fetch dynamic learning paths  
- 🔀 **Automatic Handoff** — intelligently switches between agents  
- 💬 **Chainlit UI** — chat in a user-friendly web interface  

---

## ⚙️ Getting Started

### 🔐 Prerequisites

- Python `3.8+`  
- Gemini API Key (`Google Generative Language API`)  
- Install dependencies from `requirements.txt`

---

### 🛠️ Installation


git clone https://github.com/yourusername/career-mentor-agent.git
cd career-mentor-agent
pip install -r requirements.txt
🔑 Environment Setup
Create a .env file in the root directory:

env
Copy
Edit
GEMINI_API_KEY=your_api_key_here
💻 Run the Application
bash
Copy
Edit
chainlit run main.py
Then open 👉 http://localhost:8000 in your browser.

🗂️ Project Structure
bash
Copy
Edit
career-mentor-agent/
│
├── agents/
│   ├── main_agent.py       # 🤖 Main routing agent
│   ├── career_agent.py     # 🧭 Suggests career paths
│   ├── skill_agent.py      # 🛠️ Provides skill roadmaps
│   ├── job_agent.py        # 💼 Lists job roles
│
├── tools/
│   └── roadmap.py          # 📚 Fetches learning paths
│
├── main.py                 # 🚀 App entry point
├── .env                    # 🔐 Environment variables
├── requirements.txt        # 📦 Project dependencies
└── README.md               # 📄 You're reading it!
🧠 How It Works
🗣️ User asks a question — e.g., career advice, required skills, or job titles.

🤖 Main Agent processes input and chooses the correct sub-agent.

🔀 Smart Handoff System:

"I want to explore careers in AI" → 🧭 CareerAgent

"What skills for data analyst?" → 🛠️ SkillAgent

"What jobs are in cybersecurity?" → 💼 JobAgent

🧩 SkillAgent uses the Roadmap Tool to fetch detailed learning paths.

💬 Response is delivered to the user in real-time.

💬 Example Conversation
plaintext
Copy
Edit
👤 User: I want to explore a career in data science.
🧭 CareerAgent: Data Science offers paths like Data Scientist, ML Engineer, Analyst, etc.

👤 User: What skills should I learn to become a data analyst?
🛠️ SkillAgent: You should start with Excel, SQL, statistics, data cleaning, and visualization tools.

👤 User: What are the job roles in cybersecurity?
💼 JobAgent: Security Analyst, Pen Tester, SOC Analyst, and Security Engineer are popular roles.
📄 License
MIT License © 2025 Areeba Hammad

