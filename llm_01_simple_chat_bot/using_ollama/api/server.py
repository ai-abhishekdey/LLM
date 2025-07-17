import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

from fastapi import FastAPI
from pydantic import BaseModel


# Get environment variables 

langsmith_api_key = os.environ["LANGSMITH_API_KEY"]
langsmith_tracing = os.environ["LANGSMITH_TRACING"]

# Set Langchain project

os.environ["LANGCHAIN_PROJECT"] = "LLM_01_OLLAMA"

# Prompt template

prompt = ChatPromptTemplate.from_messages(

    [

        ("system", "you are an intellegent agent. Please answer the queries asked by the user"),
        ("user","question:{question}")
    ]
)

# LLM model from ollama


llm = OllamaLLM(model="gemma2:latest")

# Output parser

output_parser = StrOutputParser()

# Chain

chain = prompt | llm | output_parser

# FastAPI app

app = FastAPI(
    title="Ollama gemma2 Chatbot API",
    version="1.0",
    description="An API to chat with Ollama gemma2 model"
)


class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def welcome():
    return {'message':'Ollama gemma2 Chatbot API'}

@app.post("/chat")
async def chat(req: QuestionRequest):
    response = chain.invoke({"question": req.question})
    return {"response": response}
