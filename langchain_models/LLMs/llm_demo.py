import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="qwen/qwen3.6-27b",
)

result = llm.invoke("What is the capital of India?")
print(result.content)