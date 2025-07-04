# 🎧 Mood Coach

**Your AI companion for emotional well-being.**

Mood Coach is a lightweight, intelligent web app that helps users reflect on their current mood through the context of their favorite music. It generates positive affirmations, emotional reflections, or mental health tips using advanced AI models.

---

## 💡 Concept & Objective

This project is built as part of the MoodScale Software Developer Internship assignment. The aim is to blend **music**, **mood**, and **mental health** in a unique and meaningful way using AI.

Mood Coach uses your:
- 🌟 Current Mood (e.g., happy, anxious, calm)
- 🎵 Favorite Song (title or lyrics)

...to generate supportive messages based on your input. Powered by **Groq's ultra-fast LLaMA 3 model**, it provides real-time emotional feedback to support your mental well-being.

---

## 🚀 Features

- 🧠 **LLaMA 3 AI via Groq API** for lightning-fast generation
- 🎧 Mood + Song input form
- ✨ Streamlit-based user interface
- 🔄 Choose between:
  - Affirmation
  - Reflection
  - Mental Health Tip
- 🔐 Secure API key via `.env` (not pushed)

---

## 🔧 Tech Stack

| Component | Tech |
|----------|------|
| Frontend UI | Streamlit |
| AI Model | LLaMA3 (via Groq API) |
| Language | Python |
| Secrets Management | `.env` file with `.gitignore` |
| Hosting (optional) | Streamlit Cloud / Localhost |

---

## 🖥️ How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/zubair-ahmad-beigh/mood-coach-app.git
   cd mood-coach-app
Create a virtual environment

bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set your Groq API Key

Create a .env file and add:

env
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
Run the app

bash
Copy
Edit
streamlit run app.py
🔍 How It Works
User selects a mood and song title.

Chooses a response type: affirmation / reflection / mental health tip.

App creates a dynamic prompt and sends it to Groq's LLaMA3 model.

AI returns a thoughtful response instantly.

Displayed on a clean, engaging Streamlit UI.

🧪 Example Prompt Sent to LLaMA3
text
Copy
Edit
Mood: Anxious  
Song: Let It Be - The Beatles  
Type: Mental Health Tip

Prompt:
Based on the song and the mood, generate a thoughtful mental health tip to comfort the user.
🌱 Future Improvements
🎶 Spotify API Integration (fetch user’s real-time song)

📊 Emotional heatmaps or journaling charts

🔄 Save history of responses

🧠 Sentiment detection via lyrics

🌐 Deploy to Streamlit Cloud / HuggingFace Spaces

📁 Folder Structure
bash
Copy
Edit
mood-coach-app/
├── app.py              # Main Streamlit App
├── .env                # API Key (excluded from Git)
├── .gitignore          # Ignores .env and cache files
├── README.md           # You are here!
├── requirements.txt    # Dependencies
├── prompt.txt          # Template prompt format
🔐 Security Best Practices
.env file is excluded from Git using .gitignore

Groq API Key is securely loaded at runtime

No secrets or keys are pushed to GitHub

🧠 Credits
Built with ❤️ by Zubair Ahmad Beigh
Powered by:

Groq LLaMA3 API

Streamlit

📌 License
This project is submitted as part of the MoodScale Internship selection. Feel free to explore the repo and contribute ideas.
