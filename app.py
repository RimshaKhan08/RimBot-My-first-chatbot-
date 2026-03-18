import streamlit as st
from chatbot import get_response

st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
    }

    body, p, div, span {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Page setup
st.set_page_config(page_title="RimBot", page_icon="🤖", layout="wide")
st.title("🖥️ RimBot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! How can I help you?"}
    ]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Get response from your logic file
    response, updated_history = get_response(
        user_input,
        st.session_state.chat_history
    )

    st.session_state.chat_history = updated_history

    # Show AI response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
