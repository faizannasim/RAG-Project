
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from utils.embedding import embeddings
from utils.pinecone_db import index

import time
import os
from dotenv import load_dotenv

load_dotenv()

# Pinecone Vector Store
vectorStore = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

# Retriever
retriever = vectorStore.as_retriever(
    search_kwargs={"k": 3}
)

# Groq LLM
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    streaming=True
)


def ask_question(question):

    # Get relevant documents from Pinecone
    docs = retriever.invoke(question)

    # Create context from retrieved documents
    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    # Prompt
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

    # Stream response and collect it
    response = ""

    for chunk in llm.stream(prompt):
        content = chunk.content

        if isinstance(content, str) and content:
            for char in content:
                print(char, end="", flush=True)
                time.sleep(0.02)
                response += char

    print()
    return response


# Run chatbot directly from query.py
if __name__ == "__main__":

    while True:
        question = input("\nAsk your question: ")

        if question.strip().lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        print("\nAnswer: ", end="", flush=True)
        answer = ask_question(question)
