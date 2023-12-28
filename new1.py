import os
import streamlit as st
from dotenv import load_dotenv
from llama_index import SimpleDirectoryReader
from llama_index import VectorStoreIndex
from llama_index import StorageContext, load_index_from_storage


def main():
    # Load environment variables from the .env file
    load_dotenv()

    # Access environment variables
    api_key = os.getenv("OPENAI_API_KEY")

    documents = SimpleDirectoryReader("./data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir="./vector_store")

    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir="./vector_store")

    # load index
    index = load_index_from_storage(storage_context)

    chat_engine = index.as_query_engine()

    st.title("ChatBot")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role":"user", "content":prompt})
        print(type(prompt))
        ######
        response = chat_engine.query(prompt)
        response = f"Bot : {response}"
        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role":"assistant", "content":response})
    
if __name__ == '__main__':
    main()