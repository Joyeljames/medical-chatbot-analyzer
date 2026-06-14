import logging
import os
from langchain_ollama import ChatOllama

LOG_DIR = "logs"

LOG_FILE = os.path.join(LOG_DIR, "RUNNING_LOGS.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class MedicalChatBot:
    def __init__(self):
        logging.info("Loading llama3")

        self.llm =ChatOllama(
            model="llama3"
        )
    
    def generate_answer(self,context,question):

        logging.info("Generating answer")

        prompt =f"""
        Answer only from context.

        Context :{context}

        Question: {question}
        """

        response = self.llm.invoke(prompt)

        return response.content