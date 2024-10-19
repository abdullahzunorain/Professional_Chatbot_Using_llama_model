
# import streamlit as st  # Import Streamlit library for web app development
# import os  # Import os module to access environment variables
# from groq import Groq  # Import Groq for interacting with the Groq API

# # Set up Groq API client
# key = os.getenv("GROQ_API")  # Get the Groq API key from environment variables
# client = Groq(api_key=key)  # Create a Groq client with the API key

# def chat(message):  # Define a function for handling chat messages
#     try:
#         chat_completion = client.chat.completions.create(  # Call the Groq API for chat completion
#             messages=[  # Prepare messages for the API
#                 {"role": "system", "content": "You are a helpful assistant."},  # System message defining assistant role
#                 {"role": "user", "content": message},  # User message
#             ],
#             model="llama3-8b-8192",  # Specify the model to use
#             temperature=0.7,  # Set the randomness of the model's responses
#             max_tokens=5000,  # Set the maximum tokens for the response
#             top_p=1,  # Set the top-p sampling for response generation
#             stop=None,  # No specific stopping conditions
#             stream=False,  # Disable streaming for responses
#         )
#         return chat_completion.choices[0].message.content  # Return the chatbot's response
#     except Exception as e:  # Handle any exceptions that occur
#         return "Sorry, something went wrong: " + str(e)  # Return error message

# # Streamlit UI
# st.title("Linguist AI: Your Professional Chatbot")  # Set the title of the app

# # Theme selection
# theme = st.selectbox(  # Create a dropdown for theme selection
#     "Select Theme:",
#     ["Default", "Gradient", "Solid Color", "Background Image"]  # List of theme options
# )

# # Set CSS based on selected theme
# if theme == "Gradient":  # If the selected theme is Gradient
#     st.markdown(  # Apply CSS for gradient background
#         """
#         <style>
#         .stApp {
#             background: linear-gradient(135deg, rgb(114, 194, 224), rgb(161, 196, 253));
#             height: 100vh;  /* Full viewport height */
#             color: black;  /* Text color */
#         }
#         </style>
#         """, unsafe_allow_html=True)  # Allow HTML/CSS rendering

# elif theme == "Solid Color":  # If the selected theme is Solid Color
#     st.markdown(  # Apply CSS for solid color background
#         """
#         <style>
#         .stApp {
#             background-color: rgb(240, 240, 240);
#             height: 100vh;  /* Full viewport height */
#             color: black;  /* Text color */
#         }
#         </style>
#         """, unsafe_allow_html=True)

# elif theme == "Background Image":  # If the selected theme is Background Image
#     st.markdown(  # Apply CSS for background image
#         """
#         <style>
#         .stApp {
#             background-image: url('https://raw.githubusercontent.com/abdullahzunorain/chatbot/main/ai-technology-brain-background-digital-transformation-concept.jpg');
#             background-size: cover;  /* Cover the entire area */
#             background-position: center;  /* Center the image */
#             height: 100vh;  /* Full viewport height */
#             color: white;  /* Text color */
#         }
#         .stTitle {
#             color: #FFFFFF !important;  /* Title color */
#             text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);  /* Shadow for title text */
#         }
#         </style>
#         """, unsafe_allow_html=True)

# else:  # Default theme
#     st.markdown(  # Apply CSS for default solid color background
#         """
#         <style>
#         .stApp {
#             background-color: rgb(255, 255, 255);
#             height: 100vh;  /* Full viewport height */
#             color: black;  /* Text color */
#         }
#         </style>
#         """, unsafe_allow_html=True)

# # Initialize chat history
# if 'history' not in st.session_state:  # Check if chat history exists in session state
#     st.session_state.history = []  # Initialize chat history list

# # Custom CSS for chat layout
# st.markdown(  # Apply custom CSS for chat layout
#     """
#     <style>
#     .chat-container {
#         max-height: 70vh;  /* Maximum height for chat container */
#         overflow-y: auto;   /* Enable vertical scrolling */
#         margin-bottom: 10px;  /* Space between chat and input */
#     }
#     .user-message {
#         background-color: #E1FFC7;  /* User message background color */
#         text-align: right;  /* Align text to the right */
#         padding: 10px;  /* Padding around message */
#         border-radius: 15px;  /* Rounded corners for message */
#         margin: 10px 0 10px 10px;  /* Margin around message */
#         display: inline-block;  /* Make it inline block */
#         max-width: 60%;  /* Maximum width for message */
#         float: right;  /* Align user messages to the right */
#         color: black;  /* Text color */
#     }
#     .bot-message {
#         background-color: #D1E7FF;  /* Bot message background color */
#         text-align: left;  /* Align text to the left */
#         padding: 10px;  /* Padding around message */
#         border-radius: 15px;  /* Rounded corners for message */
#         margin: 10px 10px 10px 0;  /* Margin around message */
#         display: inline-block;  /* Make it inline block */
#         max-width: 60%;  /* Maximum width for message */
#         float: left;  /* Align bot messages to the left */
#         color: black;  /* Text color */
#     }
#     .clearfix::after {
#         content: "";  /* Clear floats */
#         clear: both;  /* Clear both sides */
#         display: table;  /* Create a block formatting context */
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Create a form for user input
# with st.form(key='chat_form', clear_on_submit=True):  # Create a form to collect user input
#     user_input = st.text_input("You:", placeholder="Type your message here...", label_visibility="collapsed")  # Input field for user message
#     submit_button = st.form_submit_button("Send")  # Button to submit the form

# # Simulate typing indicator
# if submit_button and user_input:  # Check if the submit button is pressed and there's user input
#     with st.spinner("Linguist AI is typing..."):  # Show a spinner while waiting for a response
#         response = chat(user_input)  # Call the chat function to get a response
#         st.session_state.history.append({"user": user_input, "bot": response})  # Append the chat history

# # Display chat history in a scrollable container
# with st.container():  # Create a container for chat history
#     st.markdown('<div class="chat-container">', unsafe_allow_html=True)  # Start chat container
#     for chat in st.session_state.history:  # Loop through chat history
#         # User input style (right side now)
#         st.markdown(  # Display user message
#             f"<div class='clearfix'><div class='user-message'>{chat['user']}</div></div>",
#             unsafe_allow_html=True)
        
#         # Bot response style (left side now)
#         st.markdown(  # Display bot response
#             f"<div class='clearfix'><div class='bot-message'>{chat['bot']}</div></div>",
#             unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)  # End chat container

# # Position the input field statically at the bottom
# st.markdown(  # Apply CSS for positioning the input field
#     """
#     <style>
#     .stTextInput {
#         position: fixed;  /* Fix position of the input box */
#         bottom: 20px;  /* Adjust the distance from the bottom */
#         left: 50%;  /* Center the input box horizontally */
#         transform: translateX(-50%);  /* Shift the input box to the left by half of its width */
#         width: 60%;  /* Width of the input box */
#         z-index: 1;  /* Ensure it's above other elements */
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Position the submit button at the bottom center
# st.markdown(  # Apply CSS for positioning the button
#     """
#     <style>
#     .stFormSubmitButton {
#         position: fixed;  /* Fix position of the button */
#         bottom: 20px;  /* Adjust the distance from the bottom */
#         left: 100%;  /* Center the button horizontally */
#         transform: translateX(-50%);  /* Shift the button to the left by half of its width */
#         z-index: 1;  /* Ensure it's above other elements */
#     }
#     </style>
#     """, unsafe_allow_html=True)












import streamlit as st  # Import Streamlit library for web app development
import os  # Import os module to access environment variables
from groq import Groq  # Import Groq for interacting with the Groq API

# Set up Groq API client
key = os.getenv("GROQ_API")  # Get the Groq API key from environment variables
client = Groq(api_key=key)  # Create a Groq client with the API key

def chat(message):  # Define a function for handling chat messages
    try:
        chat_completion = client.chat.completions.create(  # Call the Groq API for chat completion
            messages=[  # Prepare messages for the API
                {"role": "system", "content": "You are a helpful assistant."},  # System message defining assistant role
                {"role": "user", "content": message},  # User message
            ],
            model="llama3-8b-8192",  # Specify the model to use
            temperature=0.7,  # Set the randomness of the model's responses
            max_tokens=5000,  # Set the maximum tokens for the response
            top_p=1,  # Set the top-p sampling for response generation
            stop=None,  # No specific stopping conditions
            stream=False,  # Disable streaming for responses
        )
        return chat_completion.choices[0].message.content  # Return the chatbot's response
    except Exception as e:  # Handle any exceptions that occur
        return "Sorry, something went wrong: " + str(e)  # Return error message

# Streamlit UI
st.title("Linguist AI: Your Professional Chatbot")  # Set the title of the app

# Theme selection
theme = st.selectbox(  # Create a dropdown for theme selection
    "Select Theme:",
    ["Default", "Gradient", "Solid Color", "Background Image"]  # List of theme options
)

# Set CSS based on selected theme
if theme == "Gradient":  # If the selected theme is Gradient
    st.markdown(  # Apply CSS for gradient background
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, rgb(114, 194, 224), rgb(161, 196, 253));
            height: 100vh;  /* Full viewport height */
            color: black;  /* Text color */
        }
        </style>
        """, unsafe_allow_html=True)  # Allow HTML/CSS rendering

elif theme == "Solid Color":  # If the selected theme is Solid Color
    st.markdown(  # Apply CSS for solid color background
        """
        <style>
        .stApp {
            background-color: rgb(240, 240, 240);
            height: 100vh;  /* Full viewport height */
            color: black;  /* Text color */
        }
        </style>
        """, unsafe_allow_html=True)

elif theme == "Background Image":  # If the selected theme is Background Image
    st.markdown(  # Apply CSS for background image
        """
        <style>
        .stApp {
            background-image: url('https://raw.githubusercontent.com/abdullahzunorain/chatbot/main/ai-technology-brain-background-digital-transformation-concept.jpg');
            background-size: cover;  /* Cover the entire area */
            background-position: center;  /* Center the image */
            height: 100vh;  /* Full viewport height */
            color: white;  /* Text color */
        }
        .stTitle {
            color: #FFFFFF !important;  /* Title color */
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);  /* Shadow for title text */
        }
        </style>
        """, unsafe_allow_html=True)

else:  # Default theme
    st.markdown(  # Apply CSS for default solid color background
        """
        <style>
        .stApp {
            background-color: rgb(255, 255, 255);
            height: 100vh;  /* Full viewport height */
            color: black;  /* Text color */
        }
        </style>
        """, unsafe_allow_html=True)

# Initialize chat history
if 'history' not in st.session_state:  # Check if chat history exists in session state
    st.session_state.history = []  # Initialize chat history list

# Custom CSS for chat layout
st.markdown(  # Apply custom CSS for chat layout
    """
    <style>
    .chat-container {
        max-height: 70vh;  /* Maximum height for chat container */
        overflow-y: auto;   /* Enable vertical scrolling */
        margin-top: 20px;  /* Space between the title and chat area */
    }
    .user-message {
        background-color: #E1FFC7;  /* User message background color */
        text-align: right;  /* Align text to the right */
        padding: 10px;  /* Padding around message */
        border-radius: 15px;  /* Rounded corners for message */
        margin: 10px 0 10px 10px;  /* Margin around message */
        display: inline-block;  /* Make it inline block */
        max-width: 60%;  /* Maximum width for message */
        float: right;  /* Align user messages to the right */
        color: black;  /* Text color */
    }
    .bot-message {
        background-color: #D1E7FF;  /* Bot message background color */
        text-align: left;  /* Align text to the left */
        padding: 10px;  /* Padding around message */
        border-radius: 15px;  /* Rounded corners for message */
        margin: 10px 10px 10px 0;  /* Margin around message */
        display: inline-block;  /* Make it inline block */
        max-width: 60%;  /* Maximum width for message */
        float: left;  /* Align bot messages to the left */
        color: black;  /* Text color */
    }
    .clearfix::after {
        content: "";  /* Clear floats */
        clear: both;  /* Clear both sides */
        display: table;  /* Create a block formatting context */
    }
    </style>
    """, unsafe_allow_html=True)

# Create a form for user input
with st.form(key='chat_form', clear_on_submit=True):  # Create a form to collect user input
    user_input = st.text_input("You:", placeholder="Type your message here...", label_visibility="collapsed")  # Input field for user message
    submit_button = st.form_submit_button("Send")  # Button to submit the form

# Simulate typing indicator
if submit_button and user_input:  # Check if the submit button is pressed and there's user input
    with st.spinner("Linguist AI is typing..."):  # Show a spinner while waiting for a response
        response = chat(user_input)  # Call the chat function to get a response
        st.session_state.history.append({"user": user_input, "bot": response})  # Append the chat history

# Display chat history in a scrollable container
with st.container():  # Create a container for chat history
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)  # Start chat container
    for chat in st.session_state.history:  # Loop through chat history
        # User input style (right side now)
        st.markdown(  # Display user message
            f"<div class='clearfix'><div class='user-message'>{chat['user']}</div></div>",
            unsafe_allow_html=True)
        
        # Bot response style (left side now)
        st.markdown(  # Display bot response
            f"<div class='clearfix'><div class='bot-message'>{chat['bot']}</div></div>",
            unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)  # End chat container

# Position the input field statically at the bottom
st.markdown(  # Apply CSS for positioning the input field
    """
    <style>
    .stTextInput {
        position: fixed;  /* Fix position of the input box */
        bottom: 20px;  /* Adjust the distance from the bottom */
        left: 40%;  /* Center the input box horizontally */
        transform: translateX(-50%);  /* Shift the input box to the left by half of its width */
        width: 60%;  /* Width of the input box */
        z-index: 1;  /* Ensure it's above other elements */
    }
    </style>
    """, unsafe_allow_html=True)

# Position the submit button at the bottom center
st.markdown(  # Apply CSS for positioning the button
    """
    <style>
    .stFormSubmitButton {
        position: fixed;  /* Fix position of the button */
        bottom: 20px;  /* Adjust the distance from the bottom */
        left: 90%;  /* Center the button horizontally */
    }
    </style>
    """, unsafe_allow_html=True)  # This line closes the previous CSS string properly
