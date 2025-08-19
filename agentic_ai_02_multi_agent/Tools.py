import os
from crewai import LLM
from crewai_tools import SerperDevTool


## Load environment variables

os.environ["OPENAI_API_KEY"]
os.environ["HF_TOKEN"]
os.environ["SERPER_API_KEY"]
os.environ["GEMINI_API_KEY"]


## Initialize serper tool

serper_tool = SerperDevTool(n_results=10)

## Load Gemini model

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
)



## Load Ollama LLM model

'''
llm = LLM(
    model="ollama/gemma2:latest",
    base_url="http://localhost:11434"
)

'''


## Load Hugging-face LLM model

'''

llm = LLM(
    model="huggingface/together/deepseek-ai/DeepSeek-R1",
    temperature=0.1
)


'''


## Load Open-AI GPT-4 LLM model

'''

llm = LLM(
    model="openai/gpt-4", # call model by provider/model_name
    temperature=0.8,
    max_tokens=150,
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1,
    stop=["END"],
    seed=42
)

'''


