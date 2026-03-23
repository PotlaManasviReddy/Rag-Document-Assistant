from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

VECTORSTORE_PATH = "data/vectorstore"

def retrieve_chunks(query, k=10):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Loading the FAISS vector store
    vectorstore = FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    results = vectorstore.similarity_search(query, k=k)

    return results


if __name__ == "__main__":
    user_query = input("Enter your question: ")
    docs = retrieve_chunks(user_query)

    print("\n Top retrieved chunks:\n")
    for i, doc in enumerate(docs, 1):
        print(f"--- Chunk {i} ---")
        print(doc.page_content[:500])
        print("\n")