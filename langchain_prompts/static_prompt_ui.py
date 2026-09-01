from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-flash-lite-latest"
)

st.header("Research Tool")

user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    result = model.invoke(user_input)

    if isinstance(result.content, str):
        st.write(result.content)
    else:
        st.write(result.content[0]["text"])