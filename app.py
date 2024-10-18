# import streamlit as st
# import os
# from groq import Groq

# # Set up Groq API client
# key = os.getenv("GROQ_API")  # Ensure your environment variable is set
# client = Groq(api_key=key)

# def chat(message):
#     try:
#         chat_completion = client.chat.completions.create(
#             messages=[
#                 {"role": "system", "content": "you are a helpful assistant."},
#                 {"role": "user", "content": message},
#             ],
#             model="llama3-8b-8192",
#             temperature=0.5,
#             max_tokens=512,  # Increased the token limit
#             top_p=1,
#             stop=None,
#             stream=False,
#         )
#         return chat_completion.choices[0].message.content
#     except Exception as e:
#         return "Sorry, something went wrong: " + str(e)

# # Streamlit UI
# st.title("Linguist AI: Your Professional Chatbot")

# st.markdown("<style> .stChatMessage {border-radius: 15px; padding: 10px;} </style>", unsafe_allow_html=True)

# if 'history' not in st.session_state:
#     st.session_state.history = []

# # Create a form for user input
# with st.form(key='chat_form', clear_on_submit=True):
#     user_input = st.text_input("You:", placeholder="Type your message here...")
#     submit_button = st.form_submit_button("Send")

# if submit_button and user_input:
#     response = chat(user_input)
#     st.session_state.history.append({"user": user_input, "bot": response})

# # Display chat history
# for chat in st.session_state.history:
#     st.markdown(f"<div class='stChatMessage' style='background-color: #E1FFC7; margin: 5px 0; border-radius: 10px; padding: 10px;'>{chat['user']}</div>", unsafe_allow_html=True)
#     st.markdown(f"<div class='stChatMessage' style='background-color: #D1E7FF; margin: 5px 0; border-radius: 10px; padding: 10px;'>{chat['bot']}</div>", unsafe_allow_html=True)



























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
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
            model="llama3-8b-8192",
            temperature=st.session_state.temperature,  # Use dynamic temperature
            max_tokens=st.session_state.max_tokens,    # Use dynamic max_tokens
            top_p=1,
            stop=None,
            stream=False,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Sorry, something went wrong: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="Linguist AI", page_icon="🤖", layout="wide")
st.title("Linguist AI: Your Professional Chatbot")

# Initialize session state variables if not already set
if 'history' not in st.session_state:
    st.session_state.history = []
if 'temperature' not in st.session_state:
    st.session_state.temperature = 0.5  # Default temperature
if 'max_tokens' not in st.session_state:
    st.session_state.max_tokens = 512    # Default max tokens

# Custom CSS for chat messages
st.markdown("""
    <style>
        .user-message {
            background-color: #E1FFC7;
            border-radius: 15px;
            padding: 10px;
            margin: 5px 0;
            max-width: 80%;
            align-self: flex-end;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        .bot-message {
            background-color: #D1E7FF;
            border-radius: 15px;
            padding: 10px;
            margin: 5px 0;
            max-width: 80%;
            align-self: flex-start;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        .chat-container {
            display: flex;
            flex-direction: column;
            height: 70vh;
            overflow-y: auto;
            border: 1px solid #d3d3d3;
            border-radius: 10px;
            padding: 10px;
            background-color: #fff;
        }
    </style>
    """, unsafe_allow_html=True)

# Chat history container
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
for chat in st.session_state.history:
    st.markdown(f"<div class='user-message'>{chat['user']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='bot-message'>{chat['bot']}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Create a form for user input
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Type your message here...")
    submit_button = st.form_submit_button("Send")

# Handle user input
if submit_button and user_input:
    response = chat(user_input)
    st.session_state.history.append({"user": user_input, "bot": response})

# Sidebar for settings
st.sidebar.header("Settings")
st.sidebar.subheader("Customize Your Chatbot")
st.session_state.temperature = st.sidebar.slider("Response Creativity (Temperature)", 0.0, 1.0, st.session_state.temperature, 0.1)
st.session_state.max_tokens = st.sidebar.slider("Max Tokens", 50, 1000, st.session_state.max_tokens, 50)

# Add a footer
st.markdown("<footer style='text-align:center; font-size: 12px; color: #888;'>Built with ❤️ by your friendly chatbot</footer>", unsafe_allow_html=True)
