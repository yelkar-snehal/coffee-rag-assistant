# Coffee RAG Assistant

## Overview
A simple Retrieval-Augmented Generation (RAG) system that helps users explore and query coffee recipes using natural language.

## Features
- Semantic search over coffee recipes
- Embedding-based retrieval using FAISS
- Natural language responses based on retrieved data

## Tech Stack
- Python
- FastAPI
- FAISS (vector database)
- sentence-transformers (embeddings)

## Example Queries
- "Sweet coffee under 5 minutes"
- "Fruity light roast recipe"
- "Low acidity coffee method"

## Architecture
Upload/Load Data → Chunk → Embed → Store (FAISS)

Query → Embed → Retrieve → Generate Response

## Future Improvements
- Add frontend (React)
- Improve ranking and filtering
- Add more datasets

## Setup Instructions

1. Clone the repository

```bash
git clone git@github.com:yelkar-snehal/coffee-rag-assistant.git
cd coffee-rag-assistant
```

2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
uvicorn app.main:app --reload
```

5. Open in browser

```text
http://127.0.0.1:8000
```
