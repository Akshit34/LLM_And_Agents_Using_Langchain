from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn
#from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM

from langserve import add_routes
  # this should be a valid Runnable

from langchain.schema import HumanMessage
from langchain.schema.runnable import RunnableLambda



import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
#langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description = "A simple API Server"
)

#add_routes(app, my_chain, path="/chain")

# add_routes(
#     app,
#     ChatGoogleGenerativeAI(),
#     path = "/geminiai"
# )

#model = ChatGoogleGenerativeAI()
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-thinking-exp-01-21")

llm1 = OllamaLLM(model="llama3")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")

chain = RunnableLambda(lambda x: llm.invoke([HumanMessage(content=x["input"])]))

add_routes(
    app,
    prompt1|chain,
    path="/essay"
)

# add_routes(
#     app,
#     prompt2|llm1,
#     path="/poem"
# )

if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)




