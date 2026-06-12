from src.components.embedding import EmbeddingGenerator
from src.components.chunking import textchunk
import numpy as np


with open("artifacts/clean_text/clean_report.txt","r",
          encoding="latin-1") as f:
    
    text = f.read()

chunker = textchunk()
embedding= EmbeddingGenerator()

chunking = chunker.create_chunks(text)
sentence_embedding = embedding.generate_embedding(chunking)

print(f"Total chunks : {len(chunking)}")
print(f"totam embeeding shape: {sentence_embedding.shape}")


np.save(
    "artifacts/embeddings/chunk_embeddings.npy",
    sentence_embedding
)

print("svaed embedding sucessfully")


