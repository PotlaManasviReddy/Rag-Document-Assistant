from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from chunk import chunk_documents  # use your chunk.py

def create_vectorstore():
    chunks = chunk_documents() 
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local("data/vectorstore")
    print("Vector store created successfully!")

if __name__ == "__main__":
    create_vectorstore()