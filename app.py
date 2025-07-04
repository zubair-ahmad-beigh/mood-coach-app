import streamlit as st
from dotenv import load_dotenv
from groq import Groq
import os

# Load environment variables
load_dotenv()

# Create Groq client using your API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Load prompt template
with open("prompt.txt", "r") as file:
    base_prompt = file.read()

# Streamlit UI setup
st.set_page_config(page_title="🎧 Mood Coach", layout="centered")

st.markdown("<h1 style='text-align: center;'>🎧 Mood Coach</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Your AI companion for emotional well-being</h4>", unsafe_allow_html=True)
st.markdown("---")

# Mood selection
st.subheader("How are you feeling right now?")
mood_options = ["😊 Happy", "😔 Sad", "😰 Anxious", "😡 Angry", "😴 Tired", "😌 Calm", "😕 Confused", "😩 Overwhelmed"]
selected_mood = st.selectbox("Choose a mood or type your own:", ["Type my own"] + mood_options)

if selected_mood == "Type my own":
    user_mood = st.text_input("Enter your mood:")
else:
    user_mood = selected_mood.split(" ", 1)[1]  # remove emoji

# Song input
song_input = st.text_input("🎵 What's your favorite song right now?", placeholder="Let It Be - The Beatles")

# Message type
mode = st.radio("What kind of message would you like?", ["Affirmation", "Reflection", "Mental Health Tip"])

# Split song input
if " - " in song_input:
    song_title, artist_name = song_input.split(" - ", 1)
else:
    song_title = song_input
    artist_name = "Unknown Artist"

# Generate message on button click
if st.button("🎤 Get My Message"):
    if not user_mood or not song_input:
        st.warning("Please fill out both the mood and the song.")
    else:
        # Prepare final prompt
        final_prompt = base_prompt.replace("{{user_mood}}", user_mood.strip()) \
                                  .replace("{{song_title}}", song_title.strip()) \
                                  .replace("{{artist_name}}", artist_name.strip())
        final_prompt += f"\n\nPlease respond in the form of a {mode.lower()}."

        with st.spinner("Generating your personalized message..."):
            try:
                response = client.chat.completions.create(
                    model="llama3-70b-8192",

                    messages=[{"role": "user", "content": final_prompt}],
                    temperature=0.85,
                    max_tokens=200,
                )
                reply = response.choices[0].message.content
                st.success("🧘 Here's your message:")
                st.markdown(f"#### 💬 {reply}")
                st.balloons()
            except Exception as e:
                st.error(f"❌ Error generating message: {e}")