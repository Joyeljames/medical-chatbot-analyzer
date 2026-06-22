from langchain_ollama import ChatOllama
import os
import logging
LOG_DIR = "logs"

LOG_FILE = os.path.join(LOG_DIR, "RUNNING_LOGS.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class SummaryGenerator:


    def __init__(self):
        self.llm = ChatOllama(
            model="llama3"
        )
    
    def generate_summary(self,report):

        prompt = f"""

     You are an expert medical assistant.

        Summarize the following medical report.

        Report:
        {report}

        Provide:

        1. Key Findings

        2. Abnormal Values

        3. Recommendations

     Keep the summary concise and easy to understand.
     """
        logging.info("generate summary")
        
        response = self.llm.invoke(prompt)

        logging.info("summary generate sucessfull")

        return response.content