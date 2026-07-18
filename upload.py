import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from utils.embedding import embeddings
#from utils.pinecone_db import index
from dotenv import load_dotenv

load_dotenv()

documents =[]

pdfs = [
    "data/AI_and_Machine_Learning_Guide.pdf",
    "data/Cloud_and_Web_Development.pdf",
    "data/Python_Programming_Handbook.pdf",
    "data/RAG_and_LangChain_Deep_Dive.pdf"
]
for pdf in pdfs:
    loader = PyPDFLoader(pdf)
    documents.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(chunk_size=500,
    chunk_overlap=100
)
chunk = splitter.split_documents(documents)
# print(chunk[0].page_content)
# print(len(chunk))


# Store Chunks in Pinecone

vector = PineconeVectorStore.from_documents(
    embedding=embeddings,
    documents = chunk,
    index_name="rag-demo"


)


# for i, chunk in enumerate(chunk):
#     print(f"Chunk {i+1}")
#     print("Source:", chunk.metadata["source"])
#     print(chunk.page_content)
#     print("-" * 80)
# print("Documents stored successfully in Pinecone!")
