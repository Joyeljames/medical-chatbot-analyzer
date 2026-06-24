from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
import logging
import os
from src.components.vectore_store import vectorstoreManager

vector = vectorstoreManager()

LOG_DIR = "logs"

LOG_FILE = os.path.join(LOG_DIR, "RUNNING_LOGS.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class RagChatBot:
    def __init__(self):
        logging.info("initializing rag chatbot for fastapi")
        self.embedding  = HuggingFaceEmbeddings(
            model_name ="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.vector_store = FAISS.load_local("artifacts/faiss_index",embeddings=self.embedding,allow_dangerous_deserialization=True)

        self.retriever = self.vector_store.as_retriever(search_kwargs={"k":3})

        self.llm = ChatOllama(model="llama3")

    
    def answerquery(self,query):
        doc = self.retriever.invoke(query)

        context = "\n".join([docs.page_content for docs in doc])
        prompt = f"""
        You are an expert medical assistant.

        Use ONLY the information provided in the context below.

        Do NOT guess or infer values that are not explicitly present.

        If the answer is not found in the context, reply:
  
        "I could not find this information in the report."

        Context:
        {context}

        Question:
        {query}

        Answer clearly and accurately.
        """

        
        response = self.llm.invoke(prompt)
        logging.info("answer generated succesfully")
        return response.content
        
    def reload_vectorstore(self):
        self.vectorstore = vector.load_vectore()
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k":2})