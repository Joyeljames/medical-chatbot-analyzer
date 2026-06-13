# Day 8 – Retrieval Pipeline

## Objective

Build a retrieval system that searches the uploaded medical report and returns the most relevant chunks for a user question.

---

## Concepts Learned

### Retrieval

Retrieval is the process of finding the most relevant information from the vector database based on a user query.

Example:

Question:
What is my cholesterol level?

Retriever searches FAISS and returns the most relevant chunks.

---

### Retriever

A Retriever acts like a search engine for the uploaded PDF.

Workflow:

Question
↓
Retriever
↓
FAISS Search
↓
Relevant Chunks

---

### Similarity Search

Similarity search compares the query embedding with stored chunk embeddings and finds the closest matches.

---

### Top-K Retrieval

Instead of returning only one chunk, the retriever can return multiple relevant chunks.

Example:

k = 3

Returns the top 3 most relevant chunks.

---

## Tasks Completed

1. Loaded the HuggingFace embedding model.
2. Loaded the FAISS vector database.
3. Created a Retriever using LangChain.
4. Tested retrieval using sample questions.
5. Retrieved relevant chunks from the medical report.
6. Created a retrieval component.
7. Created a retrieval pipeline.
8. Integrated logging into the retrieval process.

---

## Files Created

src/components/retriever.py

src/pipeline/retrieval_pipeline.py

notebooks/retrieval.ipynb

---

## Project Workflow So Far

PDF Upload
↓
Text Extraction
↓
Preprocessing
↓
Chunking
↓
Embeddings
↓
FAISS Vector Store
↓
Retriever
↓
Relevant Chunks

---

## Logger Integration

Used logger to track:

* Retriever initialization
* User query received
* Retrieval started
* Retrieval completed
* Number of documents retrieved

Example:

logging.info("Retriever Initialized")

logging.info(f"Question: {query}")

logging.info(f"Retrieved {len(docs)} documents")

---

## Key Learning

The Retriever is the bridge between FAISS and the LLM.

FAISS stores information.

Retriever searches and retrieves relevant information.

Without retrieval, the chatbot cannot find the correct context from the uploaded medical report.

---

## Challenges Faced

### Error

AttributeError:
'Retreival' object has no attribute 'vectorestore'

### Cause

Incorrect assignment:

self.vectorestore = self.vectorestore

### Fix

self.vectorestore = vectorestore

---

## Outcome

Successfully built a retrieval system that can search the uploaded medical report and return relevant chunks based on user questions.

---

## Next Step

Day 9 – Ollama + Llama 3 Integration

Workflow:

Question
↓
Retriever
↓
Relevant Chunks
↓
Llama 3
↓
Generated Answer

This will transform the retrieval system into an intelligent medical report chatbot.
