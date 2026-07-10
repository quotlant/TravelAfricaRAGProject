from fastapi import FastAPI
from pydantic import BaseModel

from app.vectorstore import search_safaris
from app.rag import generate_answer

app = FastAPI(
    title = "Travel Africa RAG"
    
)


class QuestionRequest(BaseModel):
    question: str
    top_k: int = 5
    
    
@app.post("/ask") #this endpoint will take a question and return an answer based on the safari data
def ask_question(request: QuestionRequest): #this function will take a question and return an answer based on the safari data
    
    results = search_safaris(
        request.question 
    )
    
    answer = generate_answer(
        request.question,
        results
    )
    
    return {
        "question": request.question,
        "answer": answer,

    }
    
    