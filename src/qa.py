from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

VECTORSTORE_PATH = "data/vectorstore"

def answer_question(question):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        VECTORSTORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = vectorstore.similarity_search(question, k=10)

    context = "\n\n".join([doc.page_content for doc in docs])

    llm = Ollama(model="gemma3:4b")

    prompt = f"""
You are an expert data engineer and big data specialist.
Answer the following question **based ONLY on the context provided**.
- Give a clear, concise explanation suitable for someone learning Spark.
- Explain technical terms if needed.
- Do NOT make up information. If the answer is not in the context, say "I don't know".

Question: {question}

Context:
{context}

Answer:
"""

    return llm.invoke(prompt)


if __name__ == "__main__":
    q = input("Ask a question: ")
    print("\nAnswer:\n")
    print(answer_question(q))