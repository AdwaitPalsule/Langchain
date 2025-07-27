from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Optional: LangChain tracing and API key (not required for local Ollama use)
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt template for the assistant
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's queries."),
    ("user", "Question: {question}")
])

# Streamlit interface
st.title('LangChain Demo with LLaMA2 3.2B (Ollama)')
input_text = st.text_input("Ask a question:")

# Initialize Ollama LLM (adjust model name if needed)
llm = Ollama(model="llama3.2")  # Change to "llama2" if this doesn't match
output_parser = StrOutputParser()

# Create the chain
chain = prompt | llm | output_parser

# Run the chain when the user inputs a questions
if input_text:
    response = chain.invoke({"question": input_text})
    st.markdown(f"**Response:** {response}")
