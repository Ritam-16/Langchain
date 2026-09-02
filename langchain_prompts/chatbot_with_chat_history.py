from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-flash-lite-latest"
)

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == "exit":
        break
    result = model.invoke(user_input)
    chat_history.append(result.content[0]["text"])
    print("AI: ", result.content[0]["text"])

print("Chat History: ", chat_history)