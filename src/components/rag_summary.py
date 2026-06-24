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

        prompt = f"""
        You are a medical report analyzer.

        Using ONLY the provided context, generate a structured report.

        Context:
        {context}

        Return exactly these sections:

        ## Key Findings

        ## Normal / Healthy Findings

        ## Abnormal Values

        ## Recommendations

        Do not explain that you are an AI.
        Do not say "As an expert medical assistant".
        Use bullet points.
        Keep the response concise and professional.
        """

   
        response =self.llm.invoke(prompt)

        logging.info("summary generated succesfully")

        return response.content