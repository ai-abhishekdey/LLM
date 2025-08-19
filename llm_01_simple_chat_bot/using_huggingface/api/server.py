import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from fastapi import FastAPI
from pydantic import BaseModel


# Get environment variables 

hugging_face_token = os.environ["HF_TOKEN"]
langsmith_api_key = os.environ["LANGSMITH_API_KEY"]
langsmith_tracing = os.environ["LANGSMITH_TRACING"]

# Set Langchain project

os.environ["LANGCHAIN_PROJECT"] = "LLM_01_HF"

# Prompt template

prompt = ChatPromptTemplate.from_messages(

    [

        ("system", "you are an intellegent agent. Please answer the queries asked by the user"),
        ("user","question:{question}")
    ]
)

# LLM model from hugging face

hf_endpoint = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",  # let Hugging Face choose the best provider for you
)

llm = ChatHuggingFace(llm=hf_endpoint)

# Output parser

output_parser = StrOutputParser()

# Chain

chain = prompt | llm | output_parser

# FastAPI app

app = FastAPI(
    title="HF:Llama-3.1 Chatbot API",
    version="1.0",
    description="An API to chat with HF:Llama-3.1"
)


class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def welcome():
    return {'message':'HF:Llama-3.1 Chatbot API'}

@app.post("/chat")
async def chat(req: QuestionRequest):
    response = chain.invoke({"question": req.question})
    return {"response": response}
