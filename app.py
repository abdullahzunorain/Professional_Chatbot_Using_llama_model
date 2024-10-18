import streamlit as st
import os
from groq import Groq

# Set up Groq API client
key = os.getenv("GROQ_API")
client = Groq(api_key=key)

def chat(message):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "you are a helpful assistant."},
                {"role": "user", "content": message},
            ],
            model="llama3-8b-8192",
            temperature=0.5,
            max_tokens=256,
            top_p=1,
            stop=None,
            stream=False,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return "Sorry, something went wrong: " + str(e)

# Streamlit UI
st.title("Stylish Chatbot")
st.markdown("<style> .stChatMessage {border-radius: 15px; padding: 10px;} </style>", unsafe_allow_html=True)

if 'history' not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:", placeholder="Type your message here...")

if st.button("Send"):
    if user_input:
        response = chat(user_input)
        st.session_state.history.append({"user": user_input, "bot": response})
        st.text_input("You:", value="", key="new_input")  # Clear input field

# Display chat history
for chat in st.session_state.history:
    st.markdown(f"<div class='stChatMessage' style='background-color: #E1FFC7; margin: 5px 0; border-radius: 10px; padding: 10px;'>{chat['user']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='stChatMessage' style='background-color: #D1E7FF; margin: 5px 0; border-radius: 10px; padding: 10px;'>{chat['bot']}</div>", unsafe_allow_html=True)
