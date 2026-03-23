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
```
rag-doc-assistant/
│
├── data/
│ ├── raw/ # Place your input PDF documents here
│ ├── processed/ # Stores chunked documents
│ └── vectorstore/ # Stores embeddings & FAISS vector store
│
├── src/
│ ├── ingest.py # Loads PDF files
│ ├── chunk.py # Splits documents into chunks
│ ├── embed.py # Generates embeddings & vector store
│ ├── query.py # Programmatic query interface
│ ├── qa.py # Interactive question-answer interface
│ └── blobs/ # Optional: intermediate storage for processed data
│
├── venv/ # Local virtual environment (do NOT upload)
├── requirements.txt # Project dependencies
└── README.md # Project documentation
```

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
5. **Add your PDF documents**
     ```bash
     data/raw/
     ```
## Usage Instructions

**Step 1: Ingest PDFs**
   ```bash
python src/chunk.py
```
     
**Step 2: Chunk Documents**
   ```bash
     python src/chunk.py
```

**Step 3: Generate Embeddings & Vector Store**
  ```bash
  python src/embed.py
  ```
**Step 4: Retrieval-Only Query**
```bash
python src/query.py
```

<small>You will be prompted to enter a query at runtime.</small>

**Step 5: Full Question Answering(RAG)**
   ```bash
     python src/qa.py
```


Ask natural-language questions and receive grounded answers.

<small># Enter your question when prompted. Answers will be generated from your PDFs.</small>

## Notes

- **Embeddings:** Generated using `sentence-transformers/all-MiniLM-L6-v2`.
- **Vector Store:** FAISS is used for fast semantic search.
- **LLM:** Ollama’s `gemma3:4b` model generates answers.
- **Blobs folder:** Optional intermediate storage for processed data.
- **Virtual Environment:** Do not upload `venv/` to GitHub. Use `requirements.txt`.
- **Ollama:** Ensure the Ollama app is installed and running locally before using `qa.py`.
- **Prompting:** Uses a single-question-based prompt to produce precise answers.

## Source Material

This project was tested using content from:
   - **Spark:** The Definitive Guide(Bill Chambers & Matei Zaharia)

## What This Demonstrates
   - End-to-end RAG pipeline design
   - Practical vector search with FAISS
   - Real-world document QA
   - Local LLM orchestration
   - Clean project structure & reproducibility
     
