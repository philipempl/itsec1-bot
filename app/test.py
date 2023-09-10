import sys
import os
import streamlit as st
import time
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

sys.path.append(os.path.abspath('.'))

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

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
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True, input_key='question', output_key='answer')
    return ConversationalRetrievalChain.from_llm(OpenAI(temperature=0), vectordb.as_retriever(search_kwargs={'k': 6}), return_source_documents=True, memory=memory)

# Function to get user input from Streamlit's text input widget
def get_user_input(default_input="Hello, how are you?"):
    test =  st.text_input("You: ", default_input, key="input")
    return test

if __name__ == "__main__":
    # Set Streamlit page configuration
    st.set_page_config(
        page_title="Chat App: LangChain Demo",
        page_icon="📖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Create the header
    st.header("📖 Chat App: LangChain Demo")

    # Load documents and create the conversation chain
    docs = split_docs(load_docs())
    chain = load_chain(docs)

    # Initialize chat history if not already present in session state
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


    if user_input := st.chat_input("What is your question?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            

            with st.spinner('CHAT-BOT is at Work ...'):
                assistant_response = chain({"question": user_input})

            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response["answer"].split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
