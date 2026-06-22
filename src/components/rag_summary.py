from langchain_ollama import ChatOllama
import logging


import os

LOG_DIR = "logs"

LOG_FILE = os.path.join(LOG_DIR, "RUNNING_LOGS.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class RagSummarizer:
    def __init__(self):
        self.llm = ChatOllama(
            model="llama3"
        )

        logging.info("llm model instialized")
    
    def generate_summary(self,context):

        prompt  = f"""
        You are an expert medical assistant

        summarize The report

        context: {context}

        provide:
        1.Key findings

        2.Normal/Healthy Finding

        3.Abnormal Values

        4.Recommendations

        use bullets points
    """
        response =self.llm.invoke(prompt)

        logging.info("summary generated succesfully")

        return response.content