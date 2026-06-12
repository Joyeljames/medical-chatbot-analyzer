# Day 6 – Embeddings

## Objective

Convert text chunks into vector representations (embeddings) that can be searched using a vector database.

---

## Concepts Learned

* Embeddings
* Vector Representation
* Semantic Search
* Similarity Search
* Sentence Transformers
* Embedding Models

---

## Why Embeddings are Needed

Computers cannot understand text directly.

Example:

Patient cholesterol level is 220 mg/dL

The embedding model converts text into numerical vectors:

[0.12, -0.45, 0.89, ...]

These vectors capture the meaning of the text.

Later, when a user asks a question, the question is also converted into a vector and compared with document vectors to find the most relevant information.

---

## Tasks Completed

### Notebook Work

1. Created `notebooks/embeddings.ipynb`
2. Loaded cleaned medical report text.
3. Loaded chunks generated in Day 5.
4. Installed Sentence Transformers.
5. Loaded embedding model.
6. Generated embeddings for all chunks.
7. Checked embedding dimensions.
8. Generated query embeddings.
9. Saved embeddings to NumPy format.

### Modularization

10. Created `src/components/embedding.py`
11. Created `EmbeddingGenerator` class.
12. Implemented embedding generation logic.
13. Created `src/pipeline/embedding_pipe.py`
14. Connected embedding component with pipeline.

---

## Embedding Model Used

```python
sentence-transformers/all-MiniLM-L6-v2
```

### Model Information

* Lightweight
* Fast
* Free
* Produces 384-dimensional vectors
* Commonly used in RAG projects

---

## Results

Generated:

```text
Total Embedding Shape: (6, 384)
```

Meaning:

* 6 chunks generated
* Each chunk converted into a 384-dimensional vector

---

## Challenges Faced

### Embeddings Folder Error

Error:

FileNotFoundError:
No such file or directory:
artifacts/embeddings/chunk_embeddings.npy

Reason:

The embeddings folder did not exist before saving.

Solution:

Created:

artifacts/embeddings/

Successfully saved:

chunk_embeddings.npy

---

## Files Created

### Notebook

notebooks/embeddings.ipynb

### Component

src/components/embedding.py

### Pipeline

src/pipeline/embedding_pipe.py

### Output

artifacts/embeddings/chunk_embeddings.npy

---

## Workflow

PDF
↓
Text Extraction
↓
Text Cleaning
↓
Chunking
↓
Embeddings
↓
Vector Representation

---

## Key Learnings

* Embeddings convert text into numerical vectors.
* Similar meanings produce similar vectors.
* Embeddings are the foundation of semantic search.
* Every RAG application relies on embeddings.
* Vector databases store and search embeddings efficiently.

---

## Current Project Progress

Day 1 ✅ Project Setup

Day 2 ✅ PDF Extraction

Day 3 ✅ Logging + Exception Handling + Modularization

Day 4 ✅ Text Preprocessing

Day 5 ✅ Chunking

Day 6 ✅ Embeddings

---

## Next Step

Day 7 – FAISS Vector Database

Learn:

* Vector Databases
* FAISS
* Similarity Search
* Top-K Retrieval
* Storing Embeddings
* Retrieving Relevant Chunks
