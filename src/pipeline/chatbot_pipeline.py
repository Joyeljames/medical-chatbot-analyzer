from src.components.chatbot import MedicalChatBot
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import logging
import os

LOG_DIR = "logs"

LOG_FILE = os.path.join(LOG_DIR, "RUNNING_LOGS_chatbot_pipeline.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


logging.info("chatbot_pipeline satarted")

embedding_model = HuggingFaceEmbeddings(
    model_name ="sentence-transformers/all-MiniLM-L6-v2"
)

vectore_database = FAISS.load_local(
    "artifacts/Faiss",
    embedding_model,
    allow_dangerous_deserialization=True
)

retriever  = vectore_database.as_retriever(
    search_kwargs = {"k":3}
)

question = "what is my cholestrol level"
docs = retriever.invoke(question)
context = "\n\n".join(
    [doc.page_content for doc in docs]
)

bot = MedicalChatBot()
answer = bot.generate_answer(context,question)

print(answer)

logging.info("Chatbot_pipleine copmpleted")