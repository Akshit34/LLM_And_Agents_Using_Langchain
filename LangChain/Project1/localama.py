#from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

#os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
#langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


#os.environ["PATH"] = 

#Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

##streamlit framework
st.title('Langchain Demo with Genimi APi')
input_text = st.text_input("Search the topic u want")

#Ollama Llama 3.2 model
llm = Ollama(model="llama3")
output_parser= StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

# if input_text:
#     st.write(chain.invoke(question=input_text))



