import streamlit as st
import os
from groq import Groq

# Set up Groq API client
key = os.getenv("GROQ_API")  # Ensure your environment variable is set
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
            max_tokens=512,
            top_p=1,
            stop=None,
            stream=False,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return "Sorry, something went wrong: " + str(e)

# Streamlit UI
st.title("Linguist AI: Your Professional Chatbot")

# Theme selection
theme = st.selectbox(
    "Select Theme:",
    ["Default", "Gradient", "Solid Color", "Background Image"]
)

# Set CSS based on selected theme
if theme == "Gradient":
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, rgb(114, 194, 224), rgb(161, 196, 253));
            height: 100vh;
            color: black;
        }
        .chat-container {
            background-color: rgb(255, 255, 255);
            border-radius: 15px;
            padding: 20px;
            max-width: 800px;
            margin: auto;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        }
        .stChatMessage {
            color: black;
        }
        </style>
        """, unsafe_allow_html=True)

elif theme == "Solid Color":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: rgb(240, 240, 240);
            height: 100vh;
            color: black;
        }
        .chat-container {
            background-color: rgb(255, 255, 255);
            border-radius: 15px;
            padding: 20px;
            max-width: 800px;
            margin: auto;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        }
        .stChatMessage {
            color: black;
        }
        </style>
        """, unsafe_allow_html=True)

elif theme == "Background Image":
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://raw.githubusercontent.com/abdullahzunorain/chatbot/main/pexels-broderick-armbrister-1186919-6462662.jpg');
            background-size: cover;
            background-position: center;
            height: 100vh;
            color: white;
        }
        /* Ensure the title is fully white without any transparency */
        .stTitle {
            color: #FFFFFF !important;  /* Fully white color */
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);  /* Adding shadow for visibility */
        }
        .chat-container {
            background-color: rgba(0, 0, 0, 0.7);  /* Slightly darker for better contrast */
            border-radius: 15px;
            padding: 20px;
            max-width: 800px;
            margin: auto;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        }
        .stChatMessage {
            color: white;  /* Chat message color */
            text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.7);  /* Add text shadow for better contrast */
        }
        </style>
        """, unsafe_allow_html=True)

else:  # Default theme
    st.markdown(
        """
        <style>
        .stApp {
            background-color: rgb(255, 255, 255);
            height: 100vh;
            color: black;
        }
        .chat-container {
            background-color: rgb(255, 255, 255);
            border-radius: 15px;
            padding: 20px;
            max-width: 800px;
            margin: auto;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        }
        .stChatMessage {
            color: black;
        }
        </style>
        """, unsafe_allow_html=True)

if 'history' not in st.session_state:
    st.session_state.history = []

# Create a form for user input
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Type your message here...")
    submit_button = st.form_submit_button("Send")

# Simulate typing indicator
if submit_button and user_input:
    with st.spinner("Linguist AI is typing..."):
        response = chat(user_input)
        st.session_state.history.append({"user": user_input, "bot": response})

# Display chat history in a styled container
with st.container():
    for chat in st.session_state.history:
        st.markdown(
            f"<div class='chat-container'><div class='stChatMessage' style='background-color: #E1FFC7; margin: 5px 0;'>{chat['user']}</div></div>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<div class='chat-container'><div class='stChatMessage' style='background-color: #D1E7FF; margin: 5px 0;'>{chat['bot']}</div></div>",
            unsafe_allow_html=True
        )
