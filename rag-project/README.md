# AI RAG System using Endee Vector Database

## Problem

Modern AI applications need semantic search and fast retrieval.
Traditional keyword search fails when meaning is different.
We need vector search + RAG pipeline for accurate answers.

## Solution

This project implements a Retrieval Augmented Generation (RAG) system
using Endee Vector Database, free embeddings, and local LLM.

The system:

- Converts text to embeddings
- Stores embeddings in vector store
- Searches similar vectors
- Sends context to LLM
- Generates answer

## Tech Stack

- Python
- Endee Vector Database (base repo)
- Sentence Transformers
- HuggingFace Transformers
- Local LLM (distilgpt2)
- RAG pipeline

## Architecture

User Question → Embedding → Vector Search → Context → LLM → Answer

## How Endee is used

The project is built inside the forked Endee repository.
Vector search pipeline is implemented on top of Endee base.

## How to Run

