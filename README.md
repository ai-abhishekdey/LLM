

## LLM Projects

This repo contains projects related to large language models

## Getting Started:

To start with buiding llm apps, getting model API calls and monitoring the API calls, create accounts and get API keys from 

1. [OpenAI](https://platform.openai.com/api-keys)

   * Click on **Create new secret key**

2. [Hugging-Face](https://huggingface.co/login)

   * Go to **settings** -> **Access Tokens**
   
   * Click on **Create new token**

3. [LangSmith](https://smith.langchain.com/)

   * Go to **settings**

   * Click on **Create API Key**


## Setup your environment variables in bashrc

* export environment variables 

```
echo "export OPENAI_API_KEY='<your-openai-api-key>'" >> ~/.bashrc

echo "export HF_TOKEN='<your-hugging-face-token>'" >> ~/.bashrc

echo "export LANGSMITH_TRACING=true" >> ~/.bashrc

echo "export LANGSMITH_API_KEY='<your-langsmith-api-key>'" >> ~/.bashrc

```

* source bashrc


```
source ~/.bashrc

```

## Check your environment variables in a python 


```

import os


openai_api_key = os.environ["OPENAI_API_KEY"]
hugging_face_token = os.environ["HF_TOKEN"]
langsmith_api_key = os.environ["LANGSMITH_API_KEY"]
langsmith_tracing = os.environ["LANGSMITH_TRACING"]


print(f"Open-AI API key : {openai_api_key}")
print(f"Hugging-Face Access Token : {hugging_face_token}")
print(f"LangSmith API key : {langsmith_api_key}")
print(f"LangSmith tracking : {langsmith_tracing}")


```
