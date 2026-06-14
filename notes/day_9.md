# Day 9 – Ollama + Llama 3 Integration

## Objective

Integrate Ollama and Llama 3 with the Retrieval-Augmented Generation (RAG) pipeline to generate answers from medical reports.

---

## Concepts Learned

### 1. Large Language Models (LLMs)

LLMs are AI models capable of understanding and generating human language.

Examples:

* Llama 3
* GPT
* Claude
* Qwen

---

### 2. Ollama

Ollama allows running open-source LLMs locally on a laptop without paid APIs.

Benefits:

* No API cost
* Offline usage
* Local inference

---

### 3. Retrieval-Augmented Generation (RAG)

RAG combines:

Retriever + LLM

Flow:

Question
↓
Retriever
↓
Relevant Chunks
↓
Llama 3
↓
Answer

---

## Tasks Completed

1. Installed Ollama.
2. Downloaded Llama 3 model.
3. Verified Ollama setup.
4. Tested Llama 3 locally.
5. Connected LangChain with Ollama.
6. Loaded FAISS vector database.
7. Retrieved relevant chunks from medical report.
8. Created context from retrieved chunks.
9. Built prompt template.
10. Generated answers using Llama 3.
11. Added logging to chatbot component.
12. Created modular chatbot architecture.

---

## Files Created

notebooks/llm_test.ipynb

src/components/chatbot.py

src/pipeline/chatbot_pipeline.py

---

## Key Learning

FAISS retrieves relevant information.

Llama 3 generates natural language answers from the retrieved context.

Together they form a complete RAG system.

---

## Project Architecture After Day 9

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
FAISS
↓
Retriever
↓
Llama 3
↓
Answer Generation

---

## Challenges Faced

* Ollama startup delay
* GPU vs CPU verification
* CUDA initialization issues
* LangChain integration setup

---

## Outcome

Successfully built a working Retrieval-Augmented Generation pipeline using FAISS and Llama 3.

---

## Next Step

Day 10 – Medical Report Summary Generation
