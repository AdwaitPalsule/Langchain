from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv 

##OPEN_AI_API = os.getenv("OPENAI_API_KEY")
#langsmith tracking 
LANGCHAIN_TRACING_V2 = "true"
LANGCHAIN_KEY = os.getenv("Langchain_API_KEY")
#prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ('system',"You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

#streamlit framework
st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm=ChatOpenAI(model="gpt-3.5-turbo",openai_api_key="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")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))