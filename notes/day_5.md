# Day 5 – Text Chunking

## Objective

Split the cleaned medical report text into smaller chunks that can later be converted into embeddings and stored in a vector database (FAISS).

---

## Concepts Learned

* Chunking
* Chunk Size
* Chunk Overlap
* Context Preservation
* Recursive Character Text Splitter
* Retrieval-Augmented Generation (RAG)

---

## Why Chunking is Needed

Large documents cannot be efficiently searched or sent entirely to an LLM.

Instead:

PDF
↓
Extract Text
↓
Clean Text
↓
Chunk Text
↓
Embeddings
↓
FAISS
↓
Retrieve Relevant Chunk
↓
LLM Response

Chunking helps retrieve only the relevant part of a document.

---

## Tasks Completed

### Notebook Work

1. Created `notebooks/chunking.ipynb`
2. Loaded cleaned medical report text.
3. Learned the concept of chunk size and overlap.
4. Installed LangChain text splitters.
5. Created text chunks using RecursiveCharacterTextSplitter.
6. Checked the number of generated chunks.
7. Viewed chunk contents.
8. Experimented with different chunk sizes.
9. Saved chunks into artifacts folder.

### Modularization

10. Created `src/components/chunking.py`
11. Created `TextChunker` class.
12. Implemented chunk creation logic.
13. Created `src/pipeline/chunking_pipeline.py`
14. Connected chunking component with pipeline.

---

## Challenges Faced

### LangChain Import Error

Error:

No module named 'langchain.text_splitter'

Reason:

Newer versions of LangChain moved text splitters into a separate package.

Solution:

Installed:

pip install langchain-text-splitters

Used:

from langchain_text_splitters import RecursiveCharacterTextSplitter

---

### Python Module Execution Error

Error:

ModuleNotFoundError: No module named 'src'

Reason:

Pipeline was executed outside the project root directory.

Solution:

Navigate to project folder:

cd "C:\AI&ML\clean AI projects\medical-chatbot-analyzer"

Run:

python -m src.pipeline.chunking_pipeline

---

## Files Created

### Notebook

notebooks/chunking.ipynb

### Component

src/components/chunking.py

### Pipeline

src/pipeline/chunking_pipeline.py

### Output Folder

artifacts/chunks/

---

## Workflow

Clean Text
↓
Chunking
↓
Multiple Chunks
↓
Ready for Embeddings

---

## Key Learnings

* Chunking is one of the most important steps in a RAG application.
* Smaller chunks improve retrieval quality.
* Overlap prevents information loss between chunks.
* Proper chunking improves chatbot accuracy.
* Modular code improves maintainability.

---

## Current Project Progress

Day 1 ✅ Project Setup

Day 2 ✅ PDF Extraction

Day 3 ✅ Logging + Exception Handling + Modularization

Day 4 ✅ Text Preprocessing

Day 5 ✅ Chunking

---

## Next Step

Day 6 – Embeddings

Learn:

* What embeddings are
* How text becomes vectors
* Sentence Transformers
* Creating vector representations for chunks
* Preparing for FAISS vector storage
