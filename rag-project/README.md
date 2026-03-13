# AI RAG System using Endee Vector Database

## Overview

This project implements a Retrieval Augmented Generation (RAG) system built on top of the forked Endee repository.  
The system performs semantic search using embeddings, retrieves relevant context, and generates answers using a local LLM.

The goal of this project is to demonstrate how modern AI applications use vector search + RAG pipeline + LLM to answer user queries based on real data.

This project was developed as part of the AI / ML internship evaluation task, where the requirement was to build an AI application using the Endee vector database repository.

---

## Problem

Traditional keyword search fails when the meaning of the query does not exactly match the stored text.

Modern AI systems require:

- Semantic search
- Vector embeddings
- Context retrieval
- LLM-based answer generation

To solve this, we build a Retrieval Augmented Generation (RAG) pipeline.

---

## Solution

This project builds a RAG pipeline using:

- Sentence Transformers for embeddings
- Vector search implemented on top of the Endee base repository
- Local LLM using HuggingFace Transformers
- PDF loader for real-world data
- FastAPI endpoint for querying

Flow:

User Query → Embedding → Vector Search → Context → LLM → Answer

---

## Features

- Semantic search using embeddings
- Retrieval Augmented Generation (RAG)
- PDF-based knowledge source
- FastAPI API endpoint
- Local LLM (no paid API)
- Built inside forked Endee repository
- Fully local execution

---

## Architecture

User Query  
↓  
Embedding Model (SentenceTransformer)  
↓  
Vector Store (Endee Base Repo)  
↓  
Similarity Search  
↓  
Context Retrieval  
↓  
Local LLM (HuggingFace)  
↓  
Final Answer  

---

## Project Structure

rag-project/

app.py  
rag.py  
embed.py  
llm.py  
api.py  
pdf_loader.py  
data/  
sample.pdf  
requirements.txt  
README.md  

---

## How Endee is used

The project is built inside a forked version of the Endee repository.

The vector search pipeline is implemented on top of the Endee base structure, as required by the evaluation instructions.

All code is placed inside the forked repository to ensure the project follows the required workflow.

---

## Installation

Clone the forked repository:

git clone https://github.com/vikingmanas/endee.git  
cd endee/rag-project  


Create virtual environment:

python3 -m venv venv  
source venv/bin/activate  


Install dependencies:

pip install -r requirements.txt  

---

## Run RAG CLI

python3 app.py  


Example:

Ask: What is AI  
Ask: What is RAG  

---

## Run API Server

uvicorn api:app --reload  


Open in browser:

http://127.0.0.1:8000/ask?q=what is ai  

---

## Example API Response

{
  "answer": "AI stands for artificial intelligence..."
}

---

## Technologies Used

- Python
- Endee Repository (base)
- Sentence Transformers
- HuggingFace Transformers
- FastAPI
- PyPDF
- Vector embeddings
- RAG pipeline

---

## Why this project is important

This project demonstrates:

- Real-world AI pipeline
- Vector search workflow
- RAG architecture
- Local LLM integration
- API-based AI system

These are core components used in modern AI applications.

---

## Author

Manas Dubey  
B.Tech Computer Science  
GitHub: https://github.com/vikingmanas
