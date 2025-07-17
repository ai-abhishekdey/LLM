## Simple chatbot using Ollama, Open-AI and Hugging-Face models

**Author: Abhishek Dey**

## About:

In this work, a simple chatbot is developed using different LLM models from 3 different platforms:

* Open-AI : **gpt-3.5-turbo model**

* Ollama  : **gemma2:latest model**

* Hugging-face : **meta-llama/Llama-3.1-8B-Instruct model**

## Getting started:

* Create virtual environment:

```
conda create -n llm_env python=3.13

```

* Activate environment:

```
conda activate llm_env

```

* Install required packages

```
pip3 install -r requirements.txt

```

## Steps into building chatbots:

### Step-1: Import necessary libraries and set-up the environment variables

```
import os
import streamlit as st
from fastapi import FastAPI
from pydantic import BaseModel

# Get environment variables 

openai_api_key = os.environ["OPENAI_API_KEY"]
hugging_face_token = os.environ["HF_TOKEN"]
langsmith_api_key = os.environ["LANGSMITH_API_KEY"]
langsmith_tracing = os.environ["LANGSMITH_TRACING"]

# Set Langchain project

os.environ["LANGCHAIN_PROJECT"] = "LLM_01"

```

### Step-2: Create a Prompt template

```
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(

    [

        ("system", "you are an intellegent agent. Please answer the queries asked by the user"),
        ("user","question:{question}")
    ]
)

```

### Step-3: Load the LLM model

* **Open-AI**

```
from langchain_openai import ChatOpenAI

llm=ChatOpenAI(model="gpt-3.5-turbo")

```

* **Ollama**

```
from langchain_ollama import OllamaLLM

llm=OllamaLLM(model="gemma2:latest")

```
* **Hugging-face**

```
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

hf_endpoint = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",  # let Hugging Face choose the best provider for you
)

llm=ChatHuggingFace(llm=hf_endpoint)

```

### Step-4: Create an object for Output parser

```
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

```

### Step-5: Create a chain

```
chain = prompt | llm | output_parser

```

### Step-6: Invoke chain and get llm response

```
llm_response=chain.invoke({"query": query})

```

## Dive into chatbots:

* [using ollama](using_ollama)

* [using openai](using_openai)

* [using hugging-face](using_huggingface)
