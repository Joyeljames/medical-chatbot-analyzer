from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

class vectorstoreManager:
    def __init__(self):
        self.embedding =  HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    

    def create_vectore_store(self,chunks):

        vectore_store = FAISS.from_documents(chunks,self.embedding)

        vectore_store.save_local("artifacts/faiss_index")

    def load_vectore(self):

        vectore_store = FAISS.load_local("artifacts/faiss_index",self.embedding,allow_dangerous_deserialization=True)

        return vectore_store
