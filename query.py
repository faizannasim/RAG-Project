from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from utils.embedding import embeddings
import os
from utils.pinecone_db import index
import time

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
    api_key=os.getenv("GROQ_API_KEY"),
    streaming = True
)
def ask_question(question):
    docs = retriever.invoke(question)
    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
You are an AI Assistant.

If the answer is available in the provided context, use the context to answer.

If the answer is not available in the context, answer using your own knowledge.

Do not mention whether the answer came from the context or your own knowledge.
Context:
{context}

Question:
{question}

Answer:
"""

    # response = llm.invoke(prompt)
    # return response.content
   
    for chunk in llm.stream(prompt):
        print(chunk.content,end="", flush=True)
        time.sleep(0.1)

    print()

