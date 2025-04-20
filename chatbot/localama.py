from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


#Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful Assistant.Please respond to the Queries"),
        ("user","Question:{question}")
    ]
)

#Steamlit Framework

st.title('LangChain DEMO with Ollama')
input_text=st.text_input("Search the topic you want")

#LLama2 LLM
llm=Ollama(model="llama2-uncensored")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))