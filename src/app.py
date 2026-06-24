from fastapi import FastAPI
from src.entity.request_model import QueryRequest
from src.entity.response_model import QueryResponse
from src.components.rag_chatbot import RagChatBot
from src.entity.response_model import SummaryResponse
from src.components.rag_summary import RagSummarizer
from fastapi import UploadFile, File
from src.components.vectore_store import vectorstoreManager
from src.components.pdf_loader import PdfLoader
from src.components.chunking import textchunk

pdf_load = PdfLoader()
chunkng = textchunk()
vectore_store = vectorstoreManager()


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

@app.get("/summary", response_model=SummaryResponse)
def generate_summaries():

    docs = summary_generator.retriever.invoke(
        "Summarize this medical report"
    )

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    summary_response = summary_generator.generate_summary(
        context=context
    )

    return SummaryResponse(summary=summary_response)


@app.post("/upload")
def upload_pdf(file:UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path,"wb")as f:
        f.write(file.file.read())

    text=pdf_load.extract_text(file_path)
    chunks = chunkng.create_chunks(text)
    vectore_store.create_vectore_store(chunks)
    chatbot.reload_vectorstore()
    summary_generator.reload_vectores()
    

    return {"message":"PDF processed completed"}



