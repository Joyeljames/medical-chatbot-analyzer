from langchain_community.vectorstores import FAISS

class vectorstore:

    def create_vectore_store(self,chunks,embedding_model):
        vector_store = FAISS.from_texts(
            texts = chunks,
            embedding =embedding_model
        )

        return vector_store
        