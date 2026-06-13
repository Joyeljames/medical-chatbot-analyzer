from langchain_community.vectorstores import FAISS
from src.components.retreiver import Retreival

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

logging.info("Retreival pipeline started")

embedding_model = HuggingFaceEmbeddings(
    model_name ="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local("artifacts/Faiss",embedding_model,allow_dangerous_deserialization=True)

retriever = Retreival(db)

docs =retriever.rag_retrive(
    "what is cholestrol level?"
)

for doc in docs:
    print(doc.page_content)
    logging.info("Retrival-pipeline-completed")