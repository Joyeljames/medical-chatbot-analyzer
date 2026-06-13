import logging
import os

LOG_DIR = "logs"

LOG_FILE = os.path.join(LOG_DIR, "RUNNING_LOGS.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Retreival:
    def __init__(self,vectorstore):
        self.vectorestore = vectorstore

        logging.info(
            "Retreival installed"
        )
    
    def rag_retrive(self,query,k=3):
        logging.info(f"Questions: {query}")

        retrieve = self.vectorestore.as_retriever(search_kwargs= {"k":k})

        docs = retrieve.invoke(query)

        logging.info(f"retrieved {len(docs)}") 

        return docs

        
    