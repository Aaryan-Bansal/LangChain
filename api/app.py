from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

app=FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API Server" ,
    
)

llm=Ollama(model="llama2-uncensored")

prompt1=ChatPromptTemplate.from_template("write a poem about {topic} with 100 words")


add_routes(
    app,
    prompt1|llm,
    path="/poem"
    
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)
