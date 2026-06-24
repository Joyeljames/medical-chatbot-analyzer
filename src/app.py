from fastapi import FastAPI
from src.entity.request_model import QueryRequest
from src.entity.response_model import QueryResponse
from src.components.rag_chatbot import RagChatBot
from src.entity.response_model import SummaryResponse
from src.components.rag_summary import RagSummarizer

summary_generator = RagSummarizer()

app =FastAPI(title="AI MEDICAL REPORT ANALYZER")
chatbot  = RagChatBot()

@app.get("/")
def home():
    return {"message":"analyser is running"}

@app.post("/chat",response_model=QueryResponse)

def chat(request:QueryRequest):

    answer = chatbot.answerquery(request.query)

    return QueryResponse(answer=answer)

@app.get("/summary",response_model=SummaryResponse)
def generate_summaries():

    docs = chatbot.retriever.invoke("Summarize this medical report")

    context = "\n".join([doc.page_content for doc in docs])

    summary_response = summary_generator.generate_summary(context=context)

    print(summary_response)
    print(type(summary_response))


    return SummaryResponse(summary=summary_response)
      