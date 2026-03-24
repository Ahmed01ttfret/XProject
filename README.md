# ⚽ X-Football-Intelligence (Football Nation on X)
An AI-driven tactical football analyst and automated media engine.

This project leverages Gemini 1.5 Flash/meta-llama/llama-3.3-70b-instruct and Real-time Football Data APIs to generate high-engagement tactical football breakdowns and automated match analysis. Operating autonomously via GitHub Actions, the system maintains a stateful memory to ensure a diverse and non-repetitive content feed.

### 🚀 Technical Architecture
* Language: Python 3.10+
* AI Engine: Google Gemini API (Generative AI), openAi(meta-llama/llama-3.3-70b-instruct)
* Data Sources: RapidAPI (Football Data), Football-Org API
* Automation: GitHub Actions (Scheduled Workflows)
* State Management: JSON-based persistence layer for anti-repetition tracking.

### 🛠️ Key Features
* Automated Tactical Analysis: Generates expert-level insights, ranging from historical blueprints like Sacchi’s Milan to modern-day positional play and high-pressing systems.
* Data-Driven Debates: Uses historical and current statistics to fuel high-engagement discussions (e.g., comparing peak seasons of legendary strikers like Ronaldo Nazário and Thierry Henry).
* Anti-Repetition Logic: Implements a JSON buffer that tracks the last 5 posts to ensure a unique and varied content calendar, preventing duplicate delivery to followers.
* Environment Security: Full integration with GitHub Secrets to securely manage 8 distinct API keys, ensuring professional-grade security for the entire pipeline.
* Optimized Grounding: Engineered prompts that anchor the AI in the current season to prevent hallucinations and ensure all generated content aligns with the latest football realities.

### ⚙️ Setup & Installation

1. Clone the repository:
   git clone https://github.com/Ahmed01ttfret/XProject.git
   cd XProject

2. Set up a Virtual Environment:
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate

3. Install Dependencies:
   pip install -r requirements.txt

4. Environment Variables:
   Create a .env file for local development (this file is ignored by Git via .gitignore):
   GEMINI_API_KEY=your_key
   X_api_key=your_key
   X_api_secrete=your_key
   ... (and the other 5 keys)

### 🛡️ License
Distributed under the MIT License. See LICENSE for more information.

---

### 💡 Engineering Note
This project was developed with a focus on Data Integrity and Token Efficiency. By utilizing a "Context Injection" strategy, the bot remains aware of current football landscapes without the overhead of massive system prompts, ensuring high performance within GitHub Action runner limits.
