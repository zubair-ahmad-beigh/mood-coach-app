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

## 3. Install dependencies
pip install -r requirements.txt

# 4. Create a .env file and add your Groq API key
echo GROQ_API_KEY=your_groq_api_key_here > .env

# 5. Run the Streamlit app
streamlit run app.py
⚠️ Note: .env is already listed in .gitignore, so your API key will stay secure and not be pushed to GitHub.
---
##🔍 How It Works
1. User selects a mood and types a song title  
2. Chooses a message type:
   - Affirmation
   - Reflection
   - Mental Health Tip  
3. The app dynamically creates a prompt using the input  
4. The prompt is sent to Groq’s LLaMA3 model  
5. A thoughtful response is generated and shown in the Streamlit UI
---
##🧪 Example Prompt Sent to LLaMA3
Mood: Anxious  
Song: Let It Be - The Beatles  
Type: Mental Health Tip  
Prompt:
Based on the song and the mood, generate a thoughtful mental health tip to comfort the user.
---
##🌱 Future Improvements
🎶 Spotify API Integration to fetch real-time song info  
📊 Emotional heatmaps or journaling visualizations  
🧠 Sentiment detection from lyrics  
🔄 Save user history for reflection tracking  
🌐 Deploy on Streamlit Cloud or Hugging Face Spaces
---
##📁 Folder Structure
mood-coach-app/
├── app.py            # Main Streamlit app
├── .env              # API Key (excluded from Git)
├── .gitignore        # Git ignore rules
├── README.md         # This file
├── requirements.txt  # Python dependencies
├── prompt.txt        # Optional template for prompt
---
##🔐 Security Best Practices
✅ .env is listed in .gitignore and not committed  
✅ API key is securely loaded using os.getenv()  
✅ No keys or secrets are exposed in the codebase
---
##🧠 Credits
Built with ❤️ by Zubair Ahmad Beigh  
Powered by:
- Groq LLaMA3 API  
- Streamlit
---
##📌 License
This project is submitted as part of the MoodScale Internship selection.
Feel free to explore and extend the ideas.
---
