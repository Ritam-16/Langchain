from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="qwen/qwen3.6-27b",
)

result = model.invoke("What is the capital of Arunachal Pradesh?")
print(result.content)