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
st.set_page_config(page_title="Gemini Flash Chatbot", layout="centered")
st.title("⚡ Gemini 2.0 Flash Chatbot")
st.markdown("Chat with Google's Gemini 2.0 Flash model in real-time!")


# Store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# User input
user_input = st.chat_input("Type your message...")


if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})


    # Generate Gemini response
    try:
        response = model.generate_content(user_input)
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"⚠️ Error: {e}"


    # Display bot response
    st.chat_message("assistant").markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

