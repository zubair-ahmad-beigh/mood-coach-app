# 🎧 Mood Coach  
**Your AI companion for emotional well-being.**

Mood Coach is a lightweight, intelligent web app that helps users reflect on their current mood through the context of their favorite music. It generates **positive affirmations**, **emotional reflections**, or **mental health tips** using advanced AI models.

---

## 💡 Concept & Objective

This project is built as part of the **MoodScale Software Developer Internship assignment**. The aim is to blend **music**, **mood**, and **mental health** in a unique and meaningful way using AI.

Mood Coach uses your:
- 🌟 **Current Mood** (e.g., happy, anxious, calm)
- 🎵 **Favorite Song** (title or lyrics)

...to generate supportive and uplifting messages.  
It is powered by **Groq's ultra-fast LLaMA 3 model**, providing real-time emotional feedback to support your mental well-being.

---

## 🚀 Features

- 🧠 LLaMA 3 AI via **Groq API** for lightning-fast generation  
- 🎧 Mood + Song input form  
- ✨ Streamlit-based user interface  
- 🔄 Choose between: Affirmation, Reflection, or Mental Health Tip  
- 🔐 Secure API key using `.env` (excluded via `.gitignore`)

---

## 🔧 Tech Stack

| Component          | Tech                  |
|--------------------|-----------------------|
| Frontend UI        | Streamlit             |
| AI Model           | LLaMA3 (via Groq API) |
| Language           | Python                |
| Secrets Management | `.env` + `.gitignore` |
| Hosting (Optional) | Streamlit Cloud / Localhost |

---

## 🛠️ Setup & Run Instructions

Follow these simple steps to get the app running:

```bash
# 1. Clone the repository
git clone https://github.com/zubair-ahmad-beigh/mood-coach-app.git
cd mood-coach-app

# 2. Create and activate a virtual environment
python -m venv .venv

# For Windows
.venv\Scripts\activate

# For Mac/Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a .env file and add your Groq API key
echo GROQ_API_KEY=your_groq_api_key_here > .env

# 5. Run the Streamlit app
streamlit run app.py
