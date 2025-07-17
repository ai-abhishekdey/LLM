
## Chatbot API using FastAPI

**Author: Abhishek Dey**

## About:

Here we create an API in the server side and access the API endpoint using streamlit based GUI in the client side.

## Run the server using uvicorn:

* Make sure you are inside the **api** folder

```
cd api

```
* Then start the server using uvicorn. You may change the host and port numbers

```
uvicorn server:app --reload --host 0.0.0.0 --port 8006

```

* Open **http://0.0.0.0:8006** in the browser. You should see as below

<p align="left">
<img src="img/output_localhost.png" width="1080" height="480">
</p>


* Route to  **http://0.0.0.0:8006/docs** in the browser. You should see as below

<p align="left">
<img src="img/output_localhost_docs.png" width="1080" height="480">
</p>

* You can test the API here like


<p align="left">
<img src="img/output_docs_test.png" width="1080" height="480">
</p>

* Here is the response from the API. It hits the LLM model and gets the answer

<p align="left">
<img src="img/output_docs_response.png" width="1080" height="480">
</p>


## Run Streamlit GUI as client:

```
streamlit run client.py 

```

* This is how the **server-side (left)** and **client-side (right)** looks in the terminal

 
<p align="left">
<img src="img/output_server_client.png" width="1080" height="480">
</p>


* Streamlit GUI should open in the browser or else click on the local host link shown in terminal

<p align="left">
<img src="img/output_streamlit_response.png" width="1080" height="480">
</p>


