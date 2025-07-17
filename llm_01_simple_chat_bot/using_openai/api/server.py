import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from fastapi import FastAPI
from pydantic import BaseModel


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

# LLM model from open-ai


llm=ChatOpenAI(model="gpt-3.5-turbo")

# Output parser

output_parser = StrOutputParser()

# Chain

chain = prompt | llm | output_parser

# FastAPI app

app = FastAPI(
    title="Open-AI gpt-3.5-turbo Chatbot API",
    version="1.0",
    description="An API to chat with GPT-3.5"
)


class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def welcome():
    return {'message':'Open-AI gpt-3.5-turbo Chatbot API'}

@app.post("/chat")
async def chat(req: QuestionRequest):
    response = chain.invoke({"question": req.question})
    return {"response": response}