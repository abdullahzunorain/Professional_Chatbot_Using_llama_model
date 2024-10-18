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

# Set page configuration (must be the first command)
st.set_page_config(page_title="Linguist AI", page_icon="🤖", layout="wide")

# Set up Groq API client
key = os.getenv("GROQ_API")
client = Groq(api_key=key)

# Define chat function
def chat(message, temperature, max_tokens):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
            model="llama3-8b-8192",
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1,
            stop=None,
            stream=False,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return "Sorry, something went wrong: " + str(e)

# HTML and CSS for custom styling
st.markdown(
    """
    <style>
        body {
            background-color: #f7f7f9;
            color: #333;
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
        }
        .header {
            background-color: #4a90e2;
            color: white;
            padding: 10px;
            text-align: center;
            border-radius: 10px;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            height: 70vh;
            overflow-y: auto;
            border: 1px solid #d3d3d3;
            border-radius: 10px;
            background-color: #fff;
            padding: 10px;
            margin: 20px 0;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: relative;
        }
        .empty-chat {
            color: #999;
            text-align: center;
            font-size: 16px;
            margin-top: 50px;
        }
        .user-message {
            background-color: #E1FFC7;
            border-radius: 15px;
            padding: 10px;
            margin: 5px 0;
            align-self: flex-end;
            max-width: 80%;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        .bot-message {
            background-color: #D1E7FF;
            border-radius: 15px;
            padding: 10px;
            margin: 5px 0;
            align-self: flex-start;
            max-width: 80%;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        .input-container {
            display: flex;
            margin-top: 10px;
        }
        .stTextInput {
            flex-grow: 1;
            border-radius: 10px;
            padding: 10px;
            border: 1px solid #d3d3d3;
            margin-right: 10px;
        }
        .send-button {
            background-color: #4a90e2;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 10px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .send-button:hover {
            background-color: #357ab8;
        }
        footer {
            text-align: center;
            margin-top: 20px;
            font-size: 14px;
            color: #666;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header section
st.markdown("<div class='header'><h1>Linguist AI 🤖</h1></div>", unsafe_allow_html=True)

# Initialize chat history
if 'history' not in st.session_state:
    st.session_state.history = []

# Initialize parameters in session state
if 'temperature' not in st.session_state:
    st.session_state.temperature = 0.5
if 'max_tokens' not in st.session_state:
    st.session_state.max_tokens = 512

# Sidebar for settings
st.sidebar.header("Settings")
st.sidebar.subheader("Customize Chatbot")
st.session_state.temperature = st.sidebar.slider(
    "Response Creativity (Temperature)", 0.0, 1.0, st.session_state.temperature, 0.1,
    help="Higher values make the output more random."
)
st.session_state.max_tokens = st.sidebar.slider(
    "Max Tokens", 50, 1000, st.session_state.max_tokens, 50,
    help="Adjust the maximum length of the response."
)

# Chat container
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

# Display chat history or welcome message
if not st.session_state.history:
    st.markdown("<div class='empty-chat'>Welcome! Type your message above to start chatting!</div>", unsafe_allow_html=True)
else:
    for chat in st.session_state.history:
        st.markdown(f"<div class='user-message'>{chat['user']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='bot-message'>{chat['bot']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# User input form
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Type your message here...", key='user_input', placeholder="Type your message here...")
    submit_button = st.form_submit_button("Send", help="Click to send your message", type='primary')

# Handle user input
if submit_button and user_input:
    response = chat(user_input, st.session_state.temperature, st.session_state.max_tokens)
    st.session_state.history.append({"user": user_input, "bot": response})

# Add a footer
st.markdown("<footer>Need help? Just ask me!</footer>", unsafe_allow_html=True)

# Final enhancements
st.markdown("""
    <div style='text-align:center; margin-top: 20px;'>
        <p style='font-size: 12px; color: #888;'>Built with ❤️ by your friendly chatbot</p>
    </div>
""", unsafe_allow_html=True)
