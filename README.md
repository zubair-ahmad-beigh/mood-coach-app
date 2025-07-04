#🎧 Mood Coach
Your AI companion for emotional well-being.
Mood Coach is a smart web app that helps users reflect on their current mood using their favorite music. It generates affirmations, emotional reflections, or mental health tips using cutting-edge AI.

##💡 Concept & Objective
This project is built for the MoodScale Software Developer Internship. The goal is to blend music, mood, and mental health using Groq's LLaMA 3 model to offer thoughtful, real-time reflections based on user input.

##🚀 Features
🔥 Real-time generation using Groq LLaMA 3 API

🎧 Input your mood and favorite song

✨ Clean and interactive Streamlit UI

##🔁 Choose output type:

Affirmation

Reflection

Mental Health Tip

##🔐 Secure .env-based secret handling

##🔧 Tech Stack
Component	Technology
Frontend UI	Streamlit
AI Model	LLaMA3 (via Groq API)
Programming Lang	Python
Secrets Management	.env + .gitignore
Deployment (Optional)	Streamlit Cloud / Hugging Face Spaces

##📋 Prerequisites
Python 3.8+

A Groq API Key

pip (Python package manager)

##🛠️ Setup & Run Instructions
1. Clone the Repository
git clone https://github.com/zubair-ahmad-beigh/mood-coach-app.git
cd mood-coach-app
2. Create and Activate a Virtual Environment
# Create
python -m venv .venv
# Activate (Windows)
.venv\Scripts\activate
# Activate (Mac/Linux)
source .venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Add Groq API Key to Environment File
# Create .env file
echo GROQ_API_KEY=your_groq_api_key_here > .env
⚠️ .env is already in .gitignore. Your key will stay safe.

##5. Run the App
streamlit run app.py
##🔍 How It Works
User selects a mood and enters a favorite song

Chooses one of the following:
Affirmation
Reflection
Mental Health Tip
The app builds a dynamic prompt
Sends the prompt to Groq’s LLaMA3 model
The AI returns a thoughtful response
Streamlit UI displays the result instantly

##🧪 Example Prompt Sent to LLaMA3
Mood: Anxious  
Song: Let It Be - The Beatles  
Type: Mental Health Tip  

Prompt:
Based on the song and the mood, generate a thoughtful mental health tip to comfort the user.
🌱 Future Improvements
🎶 Integrate Spotify API for live song input
📊 Add emotional heatmaps & journaling charts
🔁 Save user responses for personal tracking
🧠 Sentiment detection from lyrics
🌐 Deploy to Streamlit Cloud / Hugging Face Spaces

##📁 Project Structure
bash
Copy
Edit
mood-coach-app/
├── app.py            # Main Streamlit app
├── .env              # API Key (excluded from Git)
├── .gitignore        # Git ignore rules
├── README.md         # Project documentation
├── requirements.txt  # Python dependencies
├── prompt.txt        # Prompt template (optional)
##🔐 Security Best Practices
✅ .env is ignored via .gitignore

✅ os.getenv() used to load the API key securely

✅ No sensitive data is exposed in the repo

##🚀 Deployment (Optional)
You can deploy this app using:
Streamlit Cloud
Hugging Face Spaces
Just remember to set your GROQ_API_KEY in the deployment environment variables.

##🧠 Credits
Built with ❤️ by Zubair Ahmad Beigh
Powered by:
Groq LLaMA3 API
Streamlit

##📄 License
This project is submitted as part of the MoodScale Internship and is open for learning and improvement. Feel free to explore and extend it.
