import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={
        "token": os.getenv("HF_TOKEN")
    }
)

# # Test embeddings
# vector = embeddings.embed_query("What is Python?")
# print(len(vector))
