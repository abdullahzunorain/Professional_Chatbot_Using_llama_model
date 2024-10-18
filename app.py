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



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# import streamlit as st
# import os
# import time
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

# # Set the RGB gradient background style
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background: linear-gradient(135deg, rgb(114, 194, 224), rgb(161, 196, 253)); /* Gradient background using RGB */
#         height: 100vh;
#         color: black; /* Text color */
#         font-family: Arial, sans-serif; /* Readable font */
#     }

#     .chat-container {
#         background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent white background for chat */
#         border-radius: 15px;
#         padding: 20px;
#         max-width: 800px; /* Set a max width for the chat area */
#         margin: auto; /* Center the chat area */
#         box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
#     }

#     .stChatMessage {
#         border-radius: 15px; 
#         padding: 10px;
#     }

#     input {
#         border-radius: 15px;
#         border: 1px solid rgb(114, 194, 224);
#         padding: 10px;
#         font-size: 16px; /* Increased input text size */
#     }

#     .typing {
#         color: gray;
#         font-style: italic;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# if 'history' not in st.session_state:
#     st.session_state.history = []

# # Quick reply options
# quick_replies = ["Hello", "How are you?", "Tell me a joke", "What can you do?"]

# # Create a form for user input
# with st.form(key='chat_form', clear_on_submit=True):
#     user_input = st.text_input("You:", placeholder="Type your message here...")
#     submit_button = st.form_submit_button("Send")
    
# # Display quick reply buttons
# cols = st.columns(len(quick_replies))
# for i, reply in enumerate(quick_replies):
#     if cols[i].button(reply):
#         user_input = reply
#         submit_button = True

# # Simulate typing indicator
# if submit_button and user_input:
#     with st.spinner("Linguist AI is typing..."):
#         time.sleep(1)  # Simulate response time
#         response = chat(user_input)
#         st.session_state.history.append({"user": user_input, "bot": response})

# # Display chat history in a styled container
# with st.container():
#     for chat in st.session_state.history:
#         st.markdown(
#             f"<div class='chat-container'><div class='stChatMessage' style='background-color: #E1FFC7; margin: 5px 0;'>{chat['user']}</div></div>",
#             unsafe_allow_html=True
#         )
#         st.markdown(
#             f"<div class='chat-container'><div class='stChatMessage' style='background-color: #D1E7FF; margin: 5px 0;'>{chat['bot']}</div></div>",
#             unsafe_allow_html=True
#         )








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
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 20px;
            max-width: 800px;
            margin: auto;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
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
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 20px;
            max-width: 800px;
            margin: auto;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        }
        </style>
        """, unsafe_allow_html=True)

elif theme == "Background Image":
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://raw.githubusercontent.com/abdullahzunorain/chatbot/main/lion.jpeg'); /* Use the raw URL */
            background-size: cover;
            background-position: center;
            height: 100vh;
            color: white;
        }
        .chat-container {
            background-color: rgba(0, 0, 0, 0.5);
            border-radius: 15px;
            padding: 20px;
            max-width: 800px;
            margin: auto;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
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
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 20px;
            max-width: 800px;
            margin: auto;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
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
