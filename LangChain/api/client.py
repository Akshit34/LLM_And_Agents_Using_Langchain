import requests
import streamlit as st

def get_openai_responses(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
                             json={'topic':input_text})
    return response.json()['output']['content']

st.title('Langchain Demo with GEMINI API')
input_text= st.text_input("write an essay")
if input_text:
    st.write(get_openai_responses(input_text))