from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model = "qwen/qwen3.6-27b",
    temperature = 1.5,
)

result = model.invoke("Suggest me 5 indian names")
print(result.content)