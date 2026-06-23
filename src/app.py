from fastapi import FastAPI
from src.entity.request_model import QueryRequest
from src.entity.response_model import QueryResponse
from src.components.rag_chatbot import RagChatBot

app =FastAPI(title="AI MEDICAL REPORT ANALYZER")
chatbot  = RagChatBot()

@app.get("/")
def home():
    return {"message":"analyser is running"}

@app.post("/chat",response_model=QueryResponse)

def chat(request:QueryRequest):

    answer = chatbot.answerquery(request.query)

    return QueryResponse(answer=answer)
    