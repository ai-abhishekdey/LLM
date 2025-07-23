## Deployment in local machine

**Author: Abhishek Dey**

## About:

Here we will see how to deploy the HuggingFace model based Streamlit chatbot application in local machine using docker.

## Pre-requisite:

* you need to have **Docker** installed in your local machine. To install docker installation steps, you can checkout this [link](https://cnvrg.io/how-to-setup-docker-and-nvidia-docker-2-0-on-ubuntu-18-04/)

## Step-1: Add the below modifications : 


* Create **.env** file. Add your environment variables in **.env** file

* **NOTE:** Make sure you don't add quotes ('hf_xx') in the tokens 

```

HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxx
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=lsv2_xxxxxxxxxxxxxxxxxxxxxxxxxx

```

* Add **python-dotenv** in the requirements.txt file

* Add the below two lines in **app.py** to load the environment variables from **.env** file

```
from dotenv import load_dotenv
load_dotenv()

```

* Add the hugging_face_token as below in the **app.py**


```
hf_endpoint = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",  
    huggingfacehub_api_token=hugging_face_token # add this line
)

```

## Step-2: Docker build

```

docker build -t hf-streamlit-chatbot .

```

## Step-3: Docker run:

```
docker run --env-file .env -p 8501:8501 hf-streamlit-chatbot

```

