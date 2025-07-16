import os
import argparse
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, help='model')
parser.add_argument('--query', type=str, help='query')

args = parser.parse_args()

model=args.model
query=args.query


# Get environment variables 

langsmith_api_key = os.environ["LANGSMITH_API_KEY"]
langsmith_tracing = os.environ["LANGSMITH_TRACING"]

# Set Langchain project

os.environ["LANGCHAIN_PROJECT"] = "LLM_01"

# Prompt template

prompt = ChatPromptTemplate.from_messages(

    [

        ("system", "you are an intellegent agent. Please answer the queries asked by the user"),
        ("user","query:{query}")
    ]
)

# LLM model from openai

llm=ChatOpenAI(model=model)

# Output parser

output_parser = StrOutputParser()

# Chain

chain = prompt | llm | output_parser

llm_response=chain.invoke({"query": query})

print("=========================")
print(f"Query : {query}")
print("=========================")
print("\nLLM response :\n")
print(llm_response)
print("=========================")
