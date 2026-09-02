from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-flash-lite-latest"
)

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    result = model.invoke(user_input)
    print("AI: ", result.content[0]["text"])
    # Here the chat history is not maintained, 
    # the model will not remember the previous messages
    # and we will not have the context of the conversation
    