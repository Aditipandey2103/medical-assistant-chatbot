import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()


# Read Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)


# Initialize the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")


# Streamlit setup
st.set_page_config(page_title="AI medical chatbot", layout="centered")
st.title("⚡medical assistant Chatbot")
st.markdown("Chat with your own personal AI medical assistant in real-time!")


# Store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# User input
user_input = st.chat_input("Type your message...")
# Add a system instruction (custom behavior prompt)
system_prompt = (
    "You are a helpful and knowledgeable medical assistant. "
    "You provide reliable health and medical-related advice. "
    "Always remind users that this is not a substitute for professional medical diagnosis."
)

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate Gemini response
    try:
        response = model.generate_content(
            [system_prompt, user_input]
        )
        bot_reply = response.text + "\n\n⚠️ *This is not a substitute for professional medical advice.*"
    except Exception as e:
        bot_reply = f"⚠️ Error: {e}"

    # Display bot response
    st.chat_message("assistant").markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})



    # Display bot response
    st.chat_message("assistant").markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

