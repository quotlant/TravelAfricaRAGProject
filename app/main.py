from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from app.vectorstore import search_safaris
from app.rag import generate_answer

app = FastAPI(
    title = "Travel Africa RAG"
    
)

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)


class QuestionRequest(BaseModel):
    question: str
    top_k: int = 5
    
 
 
@app.get("/")
def home():
     return {
         "message" : "Safari RAG API is running"
     }
 
 
    
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
    
    