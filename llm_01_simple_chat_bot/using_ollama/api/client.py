import streamlit as st
import requests

st.title(" Chatbot using Ollama:gemma2 via FastAPI")

API_URL = "http://localhost:8006/chat"

user_query = st.text_input("Enter your question here:")


if user_query:

    res = requests.post(API_URL, json={"question": user_query})

    if res.status_code == 200:
        llm_response = res.json()["response"]
        st.success(llm_response)

    else:
        st.error(f"Error: {res.status_code} - {res.text}")
