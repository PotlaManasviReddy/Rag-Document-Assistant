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
rag-doc-assistant/
│
├── data/
│ ├── raw/ # Place your input PDF documents here
│ └── processed/ # Stores chunked documents and vector store files
│
├── src/
│ ├── ingest.py # Loads PDF files
│ ├── chunk.py # Splits documents into chunks
│ ├── embed.py # Generates embeddings and vector store
│ ├── query.py # Programmatic querying interface
│ ├── qa.py # Interactive question-answer interface
│ └── blobs/ # Optional: intermediate storage for processed data
│
├── venv/ # Local virtual environment (excluded from GitHub)
├── requirements.txt # Project dependencies
└── README.md # Project documentation


---

## Setup Instructions

1. **Clone the project**

```bash
git clone <your-repo-url>
cd rag-doc-assistant
```

2. **Create a virtual environment**
   ``` bash
   python -m venv venv
   ```
3. **Activate the virtual environment**
   ```bash
   .\venv\Scripts\Activate.ps1
   ```
4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```   
