from fastapi import FastAPI
from pydantic import BaseModel
from query import ask_question
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
        title="RAG Chatbot API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]


)

class question(BaseModel):
    question: str


@app.get("/")
def home():
      return {
        "message": "RAG API is Running 🚀"
    }


@app.post("/chat")
def chat(data:question):
     answer = ask_question(data.question)

     return {
        "question": data.question,
        "answer": answer
    }