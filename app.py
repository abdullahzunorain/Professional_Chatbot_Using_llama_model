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
st.set_page_config(page_title="Linguist AI", page_icon="🤖", layout="wide")  # Custom page title and icon

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
            max_tokens=512,  # Increased token limit for detailed responses
            top_p=1,
            stop=None,
            stream=False,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return "Sorry, something went wrong: " + str(e)

# Background styling
st.markdown(
    """
    <style>
        .reportview-container {
            background: url('https://your-image-url.com/background.jpg') no-repeat center center fixed;  /* Replace with your background image URL */
            background-size: cover;
            color: #FFFFFF;  /* Text color */
        }
        .stChatMessage {
            border-radius: 15px;
            padding: 10px;
            margin: 5px 0;
        }
        .user {
            background-color: #E1FFC7; /* Light green for user messages */
        }
        .bot {
            background-color: #D1E7FF; /* Light blue for bot messages */
        }
        .stTextInput {
            background-color: #F0F0F0;  /* Light gray for input box */
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

if 'history' not in st.session_state:
    st.session_state.history = []

# Create a form for user input
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Type your message here...", key='user_input')
    submit_button = st.form_submit_button("Send")

if submit_button and user_input:
    response = chat(user_input)
    st.session_state.history.append({"user": user_input, "bot": response})

# Display chat history
for chat in st.session_state.history:
    st.markdown(f"<div class='stChatMessage user'>{chat['user']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='stChatMessage bot'>{chat['bot']}</div>", unsafe_allow_html=True)

# Add a footer
st.markdown("---")
st.markdown("### Need help? Just ask me!")
