"""Python file as frontend"""
import sys
import os

# Append the current directory to the system path
sys.path.append(os.path.abspath('.'))

# Import necessary libraries
import streamlit as st
import time
from app.components.sidebar import sidebar
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOllama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler                                  

# Load the conversation chain and language model
def load_chain():
    llm = ChatOllama(base_url="http://ollama:11434", 
             model="alice", 
             callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))
    chain = ConversationChain(llm=llm)
    return chain

# Get user input text
def get_text():
    input_text = st.text_input("user", "Hallo, ich bin Alice, wie kann ich dir helfen?", key="input")
    return input_text

if __name__ == "__main__":
    # Configure the Streamlit page
    st.set_page_config(
        page_title="IT Security 1: Fragen zum Kurs",
        page_icon="📖",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    # Display the header and sidebar
    st.header("📖 IT Security 1: Fragen zum Kurs")
    sidebar()
    
    # Load the conversation chain
    chain = load_chain()

    # Initialize session_state messages if not present
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "Hallo, ich bin Alice, wie kann ich dir helfen?"}]
    
    # Show chat messages from history upon rerunning the app
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Process user input
    if user_input := st.chat_input("Was ist deine Frage?"):
        # Add user message to the chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        # Show user message in the chat container
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

   
            
            # Simulate typing with a slight delay in milliseconds
            for section in chain.run(input=user_input).split():
                full_response += section + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        
        # Add assistant response to the chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})