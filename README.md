# 🎧 Mood Coach  
**Your AI companion for emotional well-being.**

Mood Coach is a lightweight, intelligent web app that helps users reflect on their current mood through the context of their favorite music. It generates **positive affirmations**, **emotional reflections**, or **mental health tips** using advanced AI models.

---

## 💡 Concept & Objective

This project is built as part of the **MoodScale Software Developer Internship assignment**. The aim is to blend **music**, **mood**, and **mental health** in a unique and meaningful way using AI.

Mood Coach uses your:

- 🌟 **Current Mood** (e.g., happy, anxious, calm)  
- 🎵 **Favorite Song** (title or lyrics)  

...to generate supportive and uplifting messages using **Groq's ultra-fast LLaMA 3 model** to provide real-time emotional feedback.

---

## 🚀 Features

- 🧠 LLaMA 3 AI via **Groq API** for lightning-fast generation
- 🎧 Mood + Song input form
- ✨ Streamlit-based user interface
- 🔄 Choose between:
  - Affirmation  
  - Reflection  
  - Mental Health Tip
- 🔐 Secure API key using `.env` (excluded from Git)

---

## 🔧 Tech Stack

| Component          | Tech                  |
|--------------------|-----------------------|
| Frontend UI        | Streamlit             |
| AI Model           | LLaMA3 (Groq API)     |
| Language           | Python                |
| Secrets Management | `.env` + `.gitignore` |
| Hosting (Optional) | Streamlit Cloud       |

---

## 🛠️ Setup & Run Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/zubair-ahmad-beigh/mood-coach-app.git
cd mood-coach-app
