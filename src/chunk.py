from langchain_text_splitters import RecursiveCharacterTextSplitter
from ingest import load_pdf
import os
import json


def chunk_documents():
    documents = load_pdf()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    print(f"Total chunks created: {len(chunks)}")
    print("\nPreview of first chunk:\n")
    print(chunks[0].page_content[:300])

    save_chunks(chunks)
    return chunks

def save_chunks(chunks, output_path="data/processed/chunks.json"):
    os.makedirs("data/processed", exist_ok=True)

    serialized_chunks = [
        {
            "content": chunk.page_content,
            "metadata": chunk.metadata
        }
        for chunk in chunks
    ]

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(serialized_chunks, f, indent=2, ensure_ascii=False)

    print(f"Chunks saved to {output_path}")


if __name__ == "__main__":
    chunk_documents()