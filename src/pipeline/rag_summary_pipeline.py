from src.components.rag_summary import RagSummarizer
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

import logging


import os

LOG_DIR = "logs"

LOG_FILE = os.path.join(LOG_DIR, "RUNNING_LOGS.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("rag summarizer pipeline started")

embeeding_models = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

vector_store= FAISS.load_local("artifacts/Faiss",embeddings=embeeding_models,allow_dangerous_deserialization=True)

retriever = vector_store.as_retriever(
    search_kwargs ={"k":5}
)

docs = retriever.invoke("summarize this medical report")

context = "\n".join([doc.page_content for doc in docs])

summary = RagSummarizer()
summarize  = summary.generate_summary(context)

os.makedirs("artifacts/summaries",
            exist_ok=True)

with open("artifacts/summaries/summaries_report.txt","w",encoding="utf-8") as f:
    text = f.write(summarize)
print(text)

logging.info("rag summarizer pipeline completed")
