from src.components.vectore_store import vectorstore
from langchain_huggingface import HuggingFaceEmbeddings

chunks = [
    "patient cholestrol level is 240 mg/dl",
    "hemoglobin is 12.5 g/dl"
]

embedding_model = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

builder = vectorstore()

vect_store = builder.create_vectore_store(chunks,embedding_model)

store = vect_store.save_local(
    "artifacts/Faiss"
)

print(f"sucessfully stored vectores")