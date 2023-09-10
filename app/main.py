"""Python file as frontend"""
import sys
import os

# Append the current directory to the system path
sys.path.append(os.path.abspath('.'))

# Import necessary libraries
import streamlit as st
import time
from app.components.sidebar import sidebar
from langchain.llms import Ollama
from langchain.document_loaders import DirectoryLoader
from langchain.callbacks.manager import CallbackManager
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler                                  
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Function to load documents from a directory
def load_docs(directory_path="./docs"):
    loader = DirectoryLoader(directory_path)
    return loader.load()

# Function to split documents into chunks of text
def split_docs(documents, chunk_size=1000, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_documents(documents)

# Function to load the conversation chain
def load_chain(documents):
    vectordb = Chroma.from_documents(documents, OpenAIEmbeddings(), persist_directory=".")
    vectordb.persist()
    llm = Ollama(base_url="http://ollama:11434", 
             model="alice", 
             callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True, input_key='question', output_key='answer')
    return ConversationalRetrievalChain.from_llm(llm, vectordb.as_retriever(search_kwargs={'k': 6}), return_source_documents=True, memory=memory)



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
    docs = split_docs(load_docs())
    chain = load_chain(docs)

    # Initialize chat history if not already present in session state
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Hallo, ich bin Alice. Wie kann ich dir helfen?"}]

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


    if user_input := st.chat_input("Was ist deine Frage?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            

            with st.spinner('Ich überlege ...'):
                assistant_response = chain({"question": user_input})

            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response["answer"].split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
