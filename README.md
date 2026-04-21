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
