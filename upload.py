import os

from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from utils.embedding import embeddings
#from utils.pinecone_db import index
from dotenv import load_dotenv

load_dotenv()


loader = DirectoryLoader(
    path="data",
    glob= "*.pdf",
    loader_cls=PyPDFLoader

)

documents = loader.load()
print(documents[20].metadata)


# for pdf in loader:
#     loader = PyPDFLoader(pdf)
#     documents.extend(loader.load())


# chunkING
splitter = RecursiveCharacterTextSplitter(chunk_size=500,
    chunk_overlap=100
)
chunk = splitter.split_documents(documents)


# print("First Chunk:\n")
# print(chunk[0].page_content)

# vector  = embeddings.embed_query(chunk[0].page_content)
# print("\nVector Length:", len(vector))


# print("\nFirst 10 Values:")
# print(vector[:10])



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
