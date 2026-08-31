from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity


load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
)

query = "What is the capital of India?"

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France",
    "Mumbai is the financial capital of India",
]

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)