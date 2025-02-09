# MineDroid
# Problem Statement
Chatbot to respond to text queries pertaining to various Acts, Rules, and Regulations applicable to Mining industries
## Features
1. Answers basic queries pertaining to anything in general like a smart chatbot.
2. Answers queries accurately related to rules, regulations and information about Indian Mining Industries in a detailed manner.

## Local Setup and Installation
 To get the chatbot running locally on your own device, install [Langchain](https://github.com/hwchase17/langchain) and other required dependencies:

```
pip install langchain openai chromadb tiktoken unstructured streamlit googletrans==3.1.0a0
```
Head over to `constants.py` and insert your own [OpenAI API key](https://platform.openai.com/account/api-keys).

To run the pdf_reader:
1. Create a python virtual environment and a .env file
2. Create and insert your own [replicate api key](https://replicate.com/account/api-tokens) as enviornment variable
```
REPLICATE_API_TOKEN = <your replicate api token>
```
3. Finally install all the required dependencies
```
pip install langchain tiktoken replicate streamlit_chat pypdf faiss-cpu sentence_transformers
```
## Running the bot at your terminal:
To run the chatbot load your preferred .txt file.

```
> python chatbotCore.py
Input some text:
```
To run the pdf reader type in the following command at your terminal after following the instructions given in the [Setup section](#local-setup-and-installation)

```
> streamlit run <path of your folder>.venv/pdfbot.py
```
