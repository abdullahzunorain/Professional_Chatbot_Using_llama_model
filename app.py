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
            background-image: url('https://your-image-url.com/background.jpg'); /* Replace with your background image URL */
            background-size: cover;
            background-position: center;
            color: #FFFFFF; /* Text color */
        }

        .stChatMessage {
            border-radius: 20px;
            padding: 15px;
            margin: 10px 0;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
        }

        .user {
            background-color: #E6FFC7; /* Light green for user messages */
        }

        .bot {
            background-color: #D1E7FF; /* Light blue for bot messages */
        }

        .stTextInput {
            border-radius: 15px;
            padding: 10px;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
        }

        /* Additional styles for a more attractive interface */
        .st-container {
            max-width: 800px;
            margin: 0 auto;
        }

        h1 {
            color: #333333;
            font-family: Arial, sans-serif;
            text-align: center;
        }

        p {
            color: #666666;
            font-size: 18px;
            line-height: 1.5;
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
