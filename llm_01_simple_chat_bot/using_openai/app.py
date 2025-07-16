import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# Get environment variables 

openai_api_key = os.environ["OPENAI_API_KEY"]
langsmith_api_key = os.environ["LANGSMITH_API_KEY"]
langsmith_tracing = os.environ["LANGSMITH_TRACING"]

# Set Langchain project

os.environ["LANGCHAIN_PROJECT"] = "LLM_01"

# Prompt template

prompt = ChatPromptTemplate.from_messages(

    [

        ("system", "you are an intellegent agent. Please answer the queries asked by the user"),
        ("user","question:{question}")
    ]
)

# LLM model from ollama


llm=ChatOpenAI(model="gpt-3.5-turbo")

# Output parser

output_parser = StrOutputParser()

# Chain

chain = prompt | llm | output_parser

# GUI using streamlit

import streamlit as st

st.title("Chatbot using gpt-3.5-turbo")

user_query=st.text_input("Enter your question here")

if user_query:

    llm_response=chain.invoke({"question":user_query})

    st.write(llm_response)
