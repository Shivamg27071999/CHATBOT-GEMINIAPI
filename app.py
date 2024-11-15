import streamlit as st
import google.generativeai as ai

# Configure the Generative AI
ai.configure(api_key="")
model = ai.GenerativeModel('gemini-pro')

# Initialize the chatbot and history in session state
if "chatbot" not in st.session_state:
    st.session_state.chatbot = model.start_chat(history=[])

if "history" not in st.session_state:
    st.session_state.history = []

# Streamlit App Title
st.title("Welcome to Chatbot Made by SSG")

# Display conversation history
for message in st.session_state.history:
    role, content = message
    if role == "human":
        st.chat_message("human").write(content)
    else:
        st.chat_message("ai").write(content)

# Input for user prompt
user_prompt = st.chat_input("Ask me something!")

if user_prompt:
    # Display the user's message
    st.chat_message("human").write(user_prompt)
    st.session_state.history.append(("human", user_prompt))
    
    # Get the AI's response
    response = st.session_state.chatbot.send_message(user_prompt)
    ai_response = response.text
    
    # Display the AI's message
    st.chat_message("ai").write(ai_response)
    st.session_state.history.append(("ai", ai_response))
