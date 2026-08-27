# RAG Document Assistant

## Overview

RAG Document Assistant is a local Retrieval-Augmented Generation system for asking questions about PDF documents.

The project takes a PDF, splits it into smaller chunks, converts the chunks into vector embeddings, and stores them in a FAISS index. When a user asks a question, the system searches the vector store for the most relevant chunks and passes them as context to a local LLM running through Ollama.

The current implementation uses `all-MiniLM-L6-v2` for embeddings and Gemma 3 4B for answer generation.

I used *Spark: The Definitive Guide* as the document for testing the system.

## Architecture

```text
                    PDF Document
                         |
                         v
                  PDF Ingestion
                         |
                         v
                   Text Chunking
                         |
                         v
              Sentence Transformer
              all-MiniLM-L6-v2
                         |
                         v
                  FAISS Index
                         |
                         |
                  User Question
                         |
                         v
              Question Embedding
                         |
                         v
              Similarity Search
                         |
                         v
                Relevant Chunks
                         |
                         v
                  Context + Query
                         |
                         v
                    Ollama
                         |
                         v
                   Gemma 3 4B
                         |
                         v
                   Final Answer
```

## Project Structure

```text
Rag-Document-Assistant/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── vectorstore/
│       ├── index.faiss
│       └── index.pkl
│
├── src/
│   ├── ingest.py
│   ├── chunk.py
│   ├── embed.py
│   ├── query.py
│   ├── qa.py
│   └── blobs/
│
├── Requirements.txt
└── README.md
```

## Components

### `ingest.py`

Loads the PDF document using PyPDF and prepares it for further processing.

### `chunk.py`

Splits the document into smaller chunks so that relevant sections can be retrieved instead of passing the entire document to the LLM.

### `embed.py`

Generates embeddings using `all-MiniLM-L6-v2` and builds the FAISS vector store.

The current document was split into **3,092 chunks**.

### `query.py`

Takes a user question, converts it into an embedding, and performs similarity search against the FAISS index.

It returns the most relevant document chunks.

### `qa.py`

Combines retrieval and generation.

The retrieved document chunks are provided as context to Gemma 3 4B through Ollama, which generates the final answer.

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
```

### 2. Move into the project directory

```bash
cd Rag-Document-Assistant
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r Requirements.txt
```

### 6. Install Ollama

Install Ollama and make sure it is running locally.

### 7. Download Gemma 3 4B

```bash
ollama pull gemma3:4b
```

### 8. Add a PDF

Place the PDF document inside:

```text
data/raw/
```

## Running the Project

### Step 1: Ingest the PDF

```bash
python src/ingest.py
```

### Step 2: Create document chunks

```bash
python src/chunk.py
```

### Step 3: Generate embeddings and build the FAISS index

```bash
python src/embed.py
```

### Step 4: Test retrieval

```bash
python src/query.py
```

Enter a question when prompted.

Example:

```text
What is lazy evaluation in Spark?
```

The program returns the most relevant chunks from the document.

### Step 5: Run the complete RAG pipeline

```bash
python src/qa.py
```

Enter a question when prompted.

The system retrieves relevant context from the document and uses Gemma 3 4B to generate the final answer.

## Example

### Question

```text
What is lazy evaluation in Spark?
```

### Retrieved Context

The retrieval system identifies sections of the document discussing Spark's lazy evaluation model.

### Generated Answer

```text
Lazy evaluation in Spark means that Spark does not immediately execute
transformations. Instead, it builds a computation plan and waits until
an action is triggered before executing the operations.
```

## Technical Details

### Embeddings

The project uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

The embedding model converts both document chunks and user queries into vector representations.

### Vector Search

FAISS is used for similarity search over the document embeddings.

This allows the system to retrieve relevant chunks without searching through the raw document text directly.

### Language Model

Gemma 3 4B is served locally using Ollama.

The model receives the user question together with the retrieved document context and generates the final response.

### Local Inference

The LLM runs locally through Ollama, so the document content does not need to be sent to an external LLM API during inference.

## Notes

- The PDF used during development is kept outside the GitHub repository.
- Generated vector store files do not need to be committed to the repository.
- The `venv/` directory is a local Python environment and should not be uploaded.
- Ollama must be running locally before using `qa.py`.
- The embedding model is downloaded from Hugging Face when it is first used.
- The current test document produced 3,092 chunks.

## Current Status

The current version supports:

- PDF ingestion
- Document chunking
- Semantic embeddings
- FAISS similarity search
- Local LLM inference
- Retrieval-Augmented Generation
- Interactive question answering

## Future Work

### LLM Benchmarking

Compare Gemma 3 4B and Llama 3 using the same:

- Document
- Embedding model
- FAISS index
- Questions
- Retrieved context
- Prompt structure

The comparison will measure answer quality and system performance rather than relying only on subjective output.

Planned metrics include:

- Answer correctness
- Context relevance
- Faithfulness
- Response latency
- Response length
- Performance across different question types

### Evaluation Dataset

Create a set of questions with reference answers from the source document and use the dataset to evaluate both models consistently.

### Performance Analysis

Analyze the results by question category and identify where each model performs better.

## Technologies

- Python
- LangChain
- Sentence Transformers
- FAISS
- Ollama
- Gemma 3 4B
- PyPDF