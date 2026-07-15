Travel Africa AI
This is a RAG (Retrieval-Augmented Generation) travel assistant that helps users discover African safari tours using semantic search and AI-generated responses.

Features
-CSV data ingestion and cleaning.
-ChromaDB vector database.
-Search safari tours using natural language.
-Retrieves the most relevant tour information using vector embeddings.
-FastAPI backend.
-Generates AI-powered answers based on retrieved context.
-Interactive chat interface.

![Chat Interface for the Travel Africa AI](<Travel Africa AI.png>)

Project Architecture
CSV Dataset
│
▼
Data Cleaning
│
▼
Chunking
│
▼
Embeddings
│
▼
ChromaDB
│
▼
Semantic Search
│
▼
Groq LLM
│
▼
Frontend Chat UI

Tech Stack

Backend

Python
FastAPI

AI

Sentence Transformers
ChromaDB
Groq API
RAG

Frontend

HTML
CSS
JavaScript

Data

Pandas
CSV

📂 Project Structure
TravelAfricaRAGProject/
│
├── app/
│ ├── main.py
│ ├── rag.py
│ ├── scraper.py
│ └── vectorstore.py
│
├── data/
│
├── frontend/
│
├── requirements.txt
│
└── README.md

⚙️ Installation
git clone <repo-url>

cd TravelAfricaRAGProject

python -m venv venv

source venv/bin/activate

Install depedencies
pip install -r requirements.txt

RUN the API
uvicorn app.main:app --reload

OPEN:
frontend/index.html
