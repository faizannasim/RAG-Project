from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from utils.embedding import embeddings
import os
from utils.pinecone_db import index

from dotenv import load_dotenv
load_dotenv()

vectorStore = PineconeVectorStore(
    index=index,
    embedding=embeddings
)


retriever  = vectorStore.as_retriever(
     search_kwargs={"k":3}
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)
def ask_question(question):
    docs = retriever.invoke(question)
    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
You are an AI Assistant.

Answer only from the given context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)
    return response.content

print(os.getenv("GROK_API_KEY"))