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
import time  # Import time for loading indicator

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
st.set_page_config(page_title="Linguist AI: Your Professional Chatbot", layout='wide')  # Set page layout
st.title("Linguist AI: Your Professional Chatbot")

# Custom CSS for styling
st.markdown("""
<style>
    .stChatMessage {
        border-radius: 15px; 
        padding: 10px;
        max-width: 80%; 
        margin: 5px;
        word-wrap: break-word;
    }
    .user-message {
        background-color: #E1FFC7; 
        align-self: flex-end; 
        margin-left: auto; 
    }
    .bot-message {
        background-color: #D1E7FF; 
        align-self: flex-start; 
        margin-right: auto; 
    }
    .loading {
        text-align: center; 
        font-size: 1.2em; 
        color: #007BFF; 
        margin-top: 10px;
    }
    .app-background {
        background-color: #F8F9FA; 
        padding: 20px;
    }
</style>
""", unsafe_allow_html=True)

if 'history' not in st.session_state:
    st.session_state.history = []

# Create a form for user input
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Type your message here...")
    submit_button = st.form_submit_button("Send")

# Show loading spinner and response
if submit_button and user_input:
    with st.spinner("Thinking..."):  # Show loading indicator
        time.sleep(1)  # Simulate a delay for loading
        response = chat(user_input)
    
    st.session_state.history.append({"user": user_input, "bot": response})

# Display chat history
st.markdown('<div class="app-background">', unsafe_allow_html=True)  # Background for chat area
for chat in st.session_state.history:
    st.markdown(f"<div class='stChatMessage user-message'>{chat['user']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='stChatMessage bot-message'>{chat['bot']}</div>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)  # Close the background div
