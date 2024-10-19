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
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": message},
#             ],
#             model="llama3-8b-8192",
#             temperature=0.5,
#             max_tokens=2048,
#             top_p=1,
#             stop=None,
#             stream=False,
#         )
#         return chat_completion.choices[0].message.content
#     except Exception as e:
#         return "Sorry, something went wrong: " + str(e)

# # Streamlit UI
# st.title("Linguist AI: Your Professional Chatbot")

# # Theme selection
# theme = st.selectbox(
#     "Select Theme:",
#     ["Default", "Gradient", "Solid Color", "Background Image"]
# )

# # Set CSS based on selected theme
# if theme == "Gradient":
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background: linear-gradient(135deg, rgb(114, 194, 224), rgb(161, 196, 253));
#             height: 100vh;
#             color: black;
#         }
#         </style>
#         """, unsafe_allow_html=True)

# elif theme == "Solid Color":
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-color: rgb(240, 240, 240);
#             height: 100vh;
#             color: black;
#         }
#         </style>
#         """, unsafe_allow_html=True)

# elif theme == "Background Image":
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-image: url('https://raw.githubusercontent.com/abdullahzunorain/chatbot/main/ai-technology-brain-background-digital-transformation-concept.jpg');
#             background-size: cover;
#             background-position: center;
#             height: 100vh;
#             color: white;
#         }
#         .stTitle {
#             color: #FFFFFF !important;
#             text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
#         }
#         </style>
#         """, unsafe_allow_html=True)

# else:  # Default theme
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-color: rgb(255, 255, 255);
#             height: 100vh;
#             color: black;
#         }
#         </style>
#         """, unsafe_allow_html=True)

# # Initialize chat history
# if 'history' not in st.session_state:
#     st.session_state.history = []

# # Custom CSS for chat layout
# st.markdown(
#     """
#     <style>
#     .chat-container {
#         max-height: 70vh;  /* Adjust the height as necessary */
#         overflow-y: auto;   /* Enable vertical scrolling */
#         margin-bottom: 10px;  /* Space between chat and input */
#     }
#     .user-message {
#         background-color: #E1FFC7;
#         text-align: right;
#         padding: 10px;
#         border-radius: 15px;
#         margin: 10px 0 10px 10px;
#         display: inline-block;
#         max-width: 60%;
#         float: right;  /* Align user messages to the right */
#         color: black;
#     }
#     .bot-message {
#         background-color: #D1E7FF;
#         text-align: left;
#         padding: 10px;
#         border-radius: 15px;
#         margin: 10px 10px 10px 0;
#         display: inline-block;
#         max-width: 60%;
#         float: left;  /* Align bot messages to the left */
#         color: black;
#     }
#     .clearfix::after {
#         content: "";
#         clear: both;
#         display: table;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Create a form for user input
# with st.form(key='chat_form', clear_on_submit=True):
#     user_input = st.text_input("You:", placeholder="Type your message here...", label_visibility="collapsed")
#     submit_button = st.form_submit_button("Send")

# # Simulate typing indicator
# if submit_button and user_input:
#     with st.spinner("Linguist AI is typing..."):
#         response = chat(user_input)
#         st.session_state.history.append({"user": user_input, "bot": response})

# # Display chat history in a scrollable container
# with st.container():
#     st.markdown('<div class="chat-container">', unsafe_allow_html=True)
#     for chat in st.session_state.history:
#         # User input style (right side now)
#         st.markdown(
#             f"<div class='clearfix'><div class='user-message'>{chat['user']}</div></div>",
#             unsafe_allow_html=True)
        
#         # Bot response style (left side now)
#         st.markdown(
#             f"<div class='clearfix'><div class='bot-message'>{chat['bot']}</div></div>",
#             unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)

# # Position the input field statically at the bottom
# st.markdown(
#     """
#     <style>
#     .stTextInput {
#         position: fixed;
#         bottom: 20px;  /* Adjust the distance from the bottom */
#         left: 20px;  /* Adjust the distance from the left */
#         width: 60%;  /* Width of the input box */
#         z-index: 1;  /* Make sure it's above other elements */
#     }
#     </style>
#     """, unsafe_allow_html=True)


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




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
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": message},
#             ],
#             model="llama3-8b-8192",
#             temperature=0.5,
#             max_tokens=2048,
#             top_p=1,
#             stop=None,
#             stream=False,
#         )
#         return chat_completion.choices[0].message.content
#     except Exception as e:
#         return "Sorry, something went wrong: " + str(e)

# # Streamlit UI
# st.title("Linguist AI: Your Professional Chatbot")

# # Theme selection
# theme = st.selectbox(
#     "Select Theme:",
#     ["Default", "Gradient", "Solid Color", "Background Image"]
# )

# # Set CSS based on selected theme
# if theme == "Gradient":
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background: linear-gradient(135deg, rgb(114, 194, 224), rgb(161, 196, 253));
#             height: 100vh;
#             color: black;
#         }
#         </style>
#         """, unsafe_allow_html=True)

# elif theme == "Solid Color":
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-color: rgb(240, 240, 240);
#             height: 100vh;
#             color: black;
#         }
#         </style>
#         """, unsafe_allow_html=True)

# elif theme == "Background Image":
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-image: url('https://raw.githubusercontent.com/abdullahzunorain/chatbot/main/ai-technology-brain-background-digital-transformation-concept.jpg');
#             background-size: cover;
#             background-position: center;
#             height: 100vh;
#             color: white;
#         }
#         .stTitle {
#             color: #FFFFFF !important;
#             text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
#         }
#         </style>
#         """, unsafe_allow_html=True)

# else:  # Default theme
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-color: rgb(255, 255, 255);
#             height: 100vh;
#             color: black;
#         }
#         </style>
#         """, unsafe_allow_html=True)

# # Initialize chat history
# if 'history' not in st.session_state:
#     st.session_state.history = []

# # Custom CSS for chat layout
# st.markdown(
#     """
#     <style>
#     .chat-container {
#         max-height: 70vh;  /* Adjust the height as necessary */
#         overflow-y: auto;   /* Enable vertical scrolling */
#         margin-bottom: 10px;  /* Space between chat and input */
#     }
#     .user-message {
#         background-color: #E1FFC7;
#         text-align: right;
#         padding: 10px;
#         border-radius: 15px;
#         margin: 10px 0 10px 10px;
#         display: inline-block;
#         max-width: 60%;
#         float: right;  /* Align user messages to the right */
#         color: black;
#     }
#     .bot-message {
#         background-color: #D1E7FF;
#         text-align: left;
#         padding: 10px;
#         border-radius: 15px;
#         margin: 10px 10px 10px 0;
#         display: inline-block;
#         max-width: 60%;
#         float: left;  /* Align bot messages to the left */
#         color: black;
#     }
#     .clearfix::after {
#         content: "";
#         clear: both;
#         display: table;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Create a form for user input
# with st.form(key='chat_form', clear_on_submit=True):
#     user_input = st.text_input("You:", placeholder="Type your message here...", label_visibility="collapsed")
#     submit_button = st.form_submit_button("Send")

# # Simulate typing indicator
# if submit_button and user_input:
#     with st.spinner("Linguist AI is typing..."):
#         response = chat(user_input)
#         st.session_state.history.append({"user": user_input, "bot": response})

# # Display chat history in a scrollable container
# with st.container():
#     st.markdown('<div class="chat-container">', unsafe_allow_html=True)
#     for chat in st.session_state.history:
#         # User input style (right side now)
#         st.markdown(
#             f"<div class='clearfix'><div class='user-message'>{chat['user']}</div></div>",
#             unsafe_allow_html=True)
        
#         # Bot response style (left side now)
#         st.markdown(
#             f"<div class='clearfix'><div class='bot-message'>{chat['bot']}</div></div>",
#             unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)

# # Position the input field statically at the bottom
# st.markdown(
#     """
#     <style>
#     .stTextInput {
#         position: fixed;
#         bottom: 20px;  /* Adjust the distance from the bottom */
#         left: 20px;  /* Adjust the distance from the left */
#         width: 60%;  /* Width of the input box */
#         z-index: 1;  /* Make sure it's above other elements */
#     }
#     </style>
#     """, unsafe_allow_html=True)













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
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
            model="llama3-8b-8192",
            temperature=0.5,
            max_tokens=2048,
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
theme = st.selectbox("Select Theme:", ["Default", "Gradient", "Solid Color", "Background Image"])

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
        </style>
        """,
        unsafe_allow_html=True,
    )
elif theme == "Solid Color":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: rgb(240, 240, 240);
            height: 100vh;
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
elif theme == "Background Image":
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://raw.githubusercontent.com/abdullahzunorain/chatbot/main/ai-technology-brain-background-digital-transformation-concept.jpg');
            background-size: cover;
            background-position: center;
            height: 100vh;
            color: white;
        }
        .stTitle {
            color: #FFFFFF !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    # Default theme
    st.markdown(
        """
        <style>
        .stApp {
            background-color: rgb(255, 255, 255);
            height: 100vh;
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Initialize chat history
if 'history' not in st.session_state:
    st.session_state.history = []

# Custom CSS for chat layout
st.markdown(
    """
    <style>
    /* Wider chat window */
    .gizmo .gizmo\:xl\:max-w-\[48rem\] {
        max-width: 100%;
    }

    /*Wider prompt entry*/
    .xl\:max-w-3xl {
        max-width: 96%;
    }

    /* Alternating chat background color */
    .w-full.text-token-text-primary.border-b.border-black\/10.gizmo\:border-0.dark\:border-gray-900\/50.gizmo\:dark\:border-0.bg-gray-50.gizmo\:bg-transparent.dark\:bg-\[\#444654\].gizmo\:dark\:bg-transparent {
        background: #1b1818;
        margin: 10px;
    }

    /* Remove grey space */
    .md\:h-48 {
        height: 1rem;
    }

    /* Move scrollable area up */
    [class^="react-scroll-to-bottom--"] {
        height: 87%;
        overflow-y: auto;
        width: 100%;
        overflow-x: hidden;
    }

    /* Increase side scroll bar width */
    [class^="react-scroll-to-bottom--"]::-webkit-scrollbar {
        width: 20px;
    }

    /* Increase side scroll bar thumb and scroll speed */
    [class^="react-scroll-to-bottom--"]::-webkit-scrollbar-thumb {
        min-height: 40px;
    }

    /* Remove prompt suggestions */
    button.btn.relative.btn-neutral.group.w-full.whitespace-nowrap.rounded-xl.text-left.text-gray-700.dark\:text-gray-300.md\:whitespace-normal {
        display: none;
    }

    /* Move regenerate button under the prompt input */
    .md\:items-end {
        align-items: flex-end;
        position: absolute;
        left: 0;
        bottom: -45px;
    }

    /* Add red bg color to regenerate button */
    button.btn.relative.btn-neutral.whitespace-nowrap.-z-0.border-0.md\:border {
        border-radius: 10px;
        background: #ee0008;
        border: 1px solid #ee0008;
        color: #fff;
    }

    /* Regenerate button hover */
    button.btn.relative.btn-neutral.whitespace-nowrap.-z-0.border-0.md\:border:hover {
        background: #9c1519;
        border: 1px solid #9c1519;
        transition: 0.25s;
    }

    /* Add "response" to regenerate button */
    button.btn.relative.btn-neutral.whitespace-nowrap.-z-0.border-0.md\:border .flex.w-full.gap-2.items-center.justify-center:after {
        content: "last response";
    }

    /* Increase horizontal code scroll bar height */
    .p-4.overflow-y-auto::-webkit-scrollbar {
        height: 20px;
    }

    /* Move copy code to the left side */
    .flex.items-center.relative.text-gray-200.bg-gray-800.px-4.py-2.text-xs.font-sans.justify-between.rounded-t-md {
        display: flex;
        flex-direction: row-reverse;
        justify-content: flex-end;
    }

    /* Change the copy code into a button */
    .flex.items-center.relative.text-gray-200.bg-gray-800.px-4.py-2.text-xs.font-sans.justify-between.rounded-t-md button.flex.ml-auto.gap-2 {
        margin: 0 10px 0 0;
        align-items: center;
        background: #3f51b5;
        padding: 5px 10px;
        border-radius: 5px;
        min-width: 60px;
    }

    /* Hover state for copy button */
    .flex.items-center.relative.text-gray-200.bg-gray-800.px-4.py-2.text-xs.font-sans.justify-between.rounded-t-md button.flex.ml-auto.gap-2:hover {
        background: #2196F3;
        transition: 0.25s;
    }

    /* Increase size of copy code clipboard */
    .flex.items-center.relative.text-gray-200.bg-gray-800.px-4.py-2.text-xs.font-sans.justify-between.rounded-t-md svg.h-4.w-4 {
        width: 25px;
        height: 25px;
    }

    /* Increase the size of the main copy to clipboard */
    button.flex.ml-auto.gap-2.rounded-md.p-1.hover\:bg-gray-100.hover\:text-gray-700.dark\:text-gray-400.dark\:hover\:bg-gray-700.dark\:hover\:text-gray-200.disabled\:dark\:hover\:text-gray-400 svg.h-4.w-4 {
        width: 50px;
        height: 50px;
    }

    /* Move clipboard icon below the response rating */
    .text-gray-400.flex.self-end.lg\:self-center.justify-center.mt-2.gap-2.md\:gap-3.lg\:gap-1.lg\:absolute.lg\:top-0.lg\:translate-x-full.lg\:right-0.lg\:mt-0.lg\:pl-2.visible {
        display: flex;
        flex-direction: column-reverse;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a form for user input
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Type your message here...", label_visibility="collapsed")
    submit_button = st.form_submit_button("Send")

# Simulate typing indicator
if submit_button and user_input:
    with st.spinner("Linguist AI is typing..."):
        response = chat(user_input)
        st.session_state.history.append({"user": user_input, "bot": response})

# Display chat history in a scrollable container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for chat in st.session_state.history:
    # User input style (right side now)
    st.markdown(
        f"<div class='clearfix'><div class='user-message'>{chat['user']}</div></div>",
        unsafe_allow_html=True,
    )
    # Bot response style (left side now)
    st.markdown(
        f"<div class='clearfix'><div class='bot-message'>{chat['bot']}</div></div>",
        unsafe_allow_html=True,
    )
st.markdown('</div>', unsafe_allow_html=True)

# Position the input field statically at the bottom
st.markdown(
    """
    <style>
    .stTextInput {
        position: fixed;
        bottom: 20px;  /* Adjust the distance from the bottom */
        left: 20px;  /* Adjust the distance from the left */
        width: 60%;  /* Width of the input box */
        z-index: 1;  /* Make sure it's above other elements */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

