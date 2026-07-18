from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-large-en-v1.5"
)


# vector = embeddings.embed_query("What is Python?")
# print(len(vector))