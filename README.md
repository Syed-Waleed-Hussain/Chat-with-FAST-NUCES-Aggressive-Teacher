<div align="center">

# 🤬 FAST-NUCES Strict Teacher AI
### *The Most Feared, Aggressive & Sarcastic Academic Instructor on Groq LPU™*

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Groq Powered](https://img.shields.io/badge/Inference-Groq%20LPU™-f55036?style=for-the-badge&logo=fastapi&logoColor=white)](https://groq.com)
[![FAST NUCES](https://img.shields.io/badge/FAST--NUCES-Flex%20Portal%20Approved-dc2626?style=for-the-badge)](https://nu.edu.pk)
[![UI/UX Design](https://img.shields.io/badge/Design-Crimson%20Glassmorphism-991b1b?style=for-the-badge&logo=figma&logoColor=white)](https://github.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

<p align="center">
  <b>"Dafa ho jao meri class se! Asking questions when your attendance is 68%? You are getting an F grade on the Flex portal!"</b><br>
  A hilariously strict AI chatbot inspired by the legendary aggressive professors of <b>FAST National University (FAST-NUCES)</b>. Built with <b>Streamlit</b> and powered by <b>Groq LPU™</b> for lightning-fast scoldings.
</p>

[Key Features](#-key-features) • [Faculty Personas](#-faculty-personas) • [Quickstart](#-local-installation--setup) • [Deploy to Streamlit](#-deployment-to-streamlit-cloud) • [Sample Prompts](#-sample-student-excuses)

---

</div>

## 🌟 Key Features

- 🤬 **Pure FAST-NUCES Campus Trauma:** Never lets students forget their < 80% attendance, unannounced quizzes, 11:59 PM deadlines, and zero marks on Turnitin plagiarism.
- ⚡ **Sub-Second Rage Streaming (Groq LPU™):** Streams furious scoldings and technically accurate answers at over ~300–800+ tokens/second.
- 🎨 **Award-Winning Crimson Glassmorphic UI:** Sleek obsidian & crimson theme with pulsing shortage warnings, Google *Plus Jakarta Sans* typography, and modern responsive micro-interactions.
- 🧠 **Multi-Model Support & Custom ID:** Supports `Qwen 3.8 27B`, `GPT-OSS 120B/20B`, `Llama 3.3 70B`, `Llama 3.1 8B/70B`, `DeepSeek R1 Distill`, or any custom Groq model ID.
- 🎭 **Multiple Strict Faculty Personas:** Switch between Course Instructor, Head of FYP Committee, Lab Instructor, or Attendance Incharge.
- 📥 **Disciplinary Charge Sheet Export:** Download entire chat hearings in **Markdown (`.md`)** or **JSON (`.json`)**.
- ☁️ **Cloud Ready:** Fully supports `.env` locally and Streamlit Cloud `st.secrets` for 1-click free deployment.

---

## 🎭 Faculty Personas

1. **🤬 Dr. Flex (Strict Course Instructor):** The classic, fearsome professor who threatens to drop you from the course every two minutes while solving your technical problem with brutal perfection.
2. **💀 Head of FYP Evaluation Committee:** Convinced your Final Year Project is cloned from GitHub and demands IEEE Q1 publications.
3. **📝 Brutal Lab Instructor (Zero Tolerance):** Deducts 100% marks if code indentation is imperfect or if submitted at 11:59:01 PM.
4. **📋 Attendance Incharge (Zero Medical Leave):** Rejects all medical certificates and insists 79.9% attendance is an instant 'F'.

---

## 💡 Sample Student Excuses (Starter Chips)

- 🩺 *"Sir, I had dengue fever last week. Please accept my medical certificate and mark me present."*
- ⏰ *"Sir, I was just 2 minutes late to the 8:30 AM lecture because the bus broke down."*
- 💻 *"Sir, my code has a Segmentation Fault on line 42. Please debug it."*
- 📊 *"Sir, my attendance is 79.2%. Can you please round it off to 80%?"*

---

## 🚀 Local Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Syed-Waleed-Hussain/Hero-and-Villain-Predictor-for-Marvel-and-DC-Characters-Using-Neural-Networks.git
cd "Week 6"
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add Your Groq API Key
Create a `.env` file in the folder:
```env
GROQ_API_KEY=gsk_your_actual_groq_api_key_here
```

### 4. Launch the App
```bash
streamlit run app.py
```
Open `http://localhost:8501` to face Sir!

---

## ☁️ Deployment to Streamlit Cloud

### Step 1: Commit and Push Code to GitHub
```bash
git add "Week 6"
git commit -m "feat: Add FAST NUCES Strict Teacher AI"
git push origin main
```

### Step 2: Deploy on Streamlit Community Cloud
1. Go to **[share.streamlit.io](https://share.streamlit.io/)** and sign in with GitHub.
2. Click **New app**.
3. Select your repository: `Syed-Waleed-Hussain/Hero-and-Villain-Predictor-for-Marvel-and-DC-Characters-Using-Neural-Networks`
4. Set **Branch** to `main` and **Main file path** to `Week 6/app.py`.
5. Under **Advanced settings ➡️ Secrets**, paste:
   ```toml
   GROQ_API_KEY = "gsk_your_actual_groq_api_key_here"
   ```
6. Click **Deploy!** 🚀

---

## 📁 Project Structure

```
Week 6/
├── .streamlit/
│   └── config.toml       # Streamlit dark theme settings
├── app.py                # FAST-NUCES Strict Teacher Chatbot with Glassmorphism UI
├── requirements.txt      # Streamlit, Groq, Dotenv
├── .env                  # Secret API key (local only)
├── .env.example          # Environment template
├── .gitignore            # Git rules
└── README.md             # Project documentation
```

---

<div align="center">
  <b>Built with ❤️ (and academic trauma) by Syed Waleed Hussain</b>
</div>
