#Simple TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-flash-lite-latest"
)

#schema
class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
I recently bought a new smartphone, and I'm extremely happy with it. The camera quality is outstanding, and the battery lasts all day.
""")

print(result)
print(result['summary'])
print(result['sentiment'])