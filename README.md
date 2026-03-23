# RAG Document Assistant

## Project Overview
The RAG (Retrieval-Augmented Generation) Document Assistant is a Python-based tool that allows users to query PDF documents and receive contextually relevant answers. It uses modern NLP techniques, combining:

- **Document chunking** for splitting large PDFs into manageable pieces.
- **Sentence embeddings** for semantic similarity.
- **FAISS vector store** for fast retrieval of relevant chunks.
- **Ollama’s Gemma3:4b LLM** to generate answers based on retrieved content.

The project is designed to provide a scalable, local-first QA system over your document corpus.

---

## Project Structure
