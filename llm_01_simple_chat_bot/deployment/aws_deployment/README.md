## Deployment in AWS

**Author: Abhishek Dey**

## About:

Here we will see how to deploy the HuggingFace model based Streamlit chatbot application in AWS using docker.

## Pre-requisite:

* AWS Account

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

## Step-2: Login to AWS Manangement Console

* Sign In as [Root user](https://signin.aws.amazon.com/signin?client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3FhashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_si%26src%3Dheader-signin%26state%3DhashArgsFromTB_eu-north-1_6e05766ac7e8b412&page=resolve&code_challenge=pa7LMuI9Uv1v9j3ZjDiS5ZsIViiKsTm5XrW_rN1jWy8&code_challenge_method=SHA-256&backwards_compatible=true)


* Once you enter into AWS account, search for **Elastic Beanstalk**

* Click on **Create application**

## Step-3 Setup configurations


* Click on **create role** in **Service role** section

* Click on **create role** in **EC2 instance profile**

  * Click on **next** -> **next** similar to the previous step
  
* Click on **next** -> **next** to keep default settings for the **optional configurations step 3-5**

* Finally you launch into the **Review** section

* Scroll down and click on **create**

* Around 3-4 minutes will be taken to create the environmment. Finally you should see a page like below


## zip the required files

```

zip hf_streamlit_chatbot.zip app.py Dockerfile requirements.txt .env

```


