import os
from crewai import LLM, Agent

## Load environment variables

os.environ["HF_TOKEN"]

## Load LLM model

llm = LLM(
    model="huggingface/together/deepseek-ai/DeepSeek-R1",
    temperature=0.1
)

'''
llm_out=llm.call("Who invented telescope ?")
print(llm_out)
'''

## Content writer agent



content_writer_agent=Agent(

    role="Senior Content Writer",
    goal="Write a beutiful paragraph on the given topic {topic} within 100 words",
    backstory="A highly experienced Content Writer expertised in summarizing any given topic within given word limit",
    llm=llm,
    verbose=True,
    memory=True,
    allow_delegation=False


)