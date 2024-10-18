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
                {"role": "system", "content": "you are a helpful assistant."},
                {"role": "user", "content": message},
            ],
            model="llama3-8b-8192",
            temperature=0.5,
            max_tokens=512,  # Increased the token limit
            top_p=1,
            stop=None,
            stream=False,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return "Sorry, something went wrong: " + str(e)

# Streamlit UI
st.title("Linguist AI: Your Professional Chatbot")

# Set the background image using CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('Glows.jpeg'); /* Ensure this path is correct */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh; /* Full height of the viewport */
        color: white; /* Adjust text color for better visibility */
    }
    .chat-container {
        background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent background */
        border-radius: 15px;
        padding: 20px;
        max-width: 800px; /* Set a max width for the chat area */
        margin: auto; /* Center the chat area */
    }
    .stChatMessage {
        border-radius: 15px; 
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if 'history' not in st.session_state:
    st.session_state.history = []

# Create a form for user input
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Type your message here...")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input:
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
