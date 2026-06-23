# 🚀 Day 14 - FastAPI + RAG Chatbot Integration

## Goal

Integrate the real RAG chatbot with FastAPI.

Replace the dummy response with the actual:

* FAISS Retriever
* Top K Chunks
* Llama3
* JSON Response

---

# Architecture

```text
User
↓
POST /chat
↓
FastAPI
↓
RAGChatbot Component
↓
FAISS Retriever
↓
Top K Chunks
↓
Llama3
↓
Answer
↓
JSON Response
```

---

# Component

Created:

```text
src/components/rag_chatbot.py
```

## Class

```python
RAGChatbot
```

## Method

```python
answer_query()
```

## Flow

```text
Query
↓
Retriever
↓
Top K Chunks
↓
Context
↓
Prompt
↓
Llama3
↓
Answer
```

---

# FastAPI Integration

Updated:

```text
src/app.py
```

Connected:

```python
chatbot.answer_query()
```

with:

```python
@app.post("/chat")
```

---

# Request Model

```text
src/entity/request_models.py
```

```python
class QueryRequest(BaseModel):

    query: str
```

---

# Response Model

```text
src/entity/response_models.py
```

```python
class QueryResponse(BaseModel):

    answer: str
```

---

# API Flow

Input:

```json
{
  "query":"Is my Hb normal?"
}
```

↓

```text
FastAPI
↓
QueryRequest
↓
RAGChatbot
↓
Retriever
↓
Top K Chunks
↓
Llama3
↓
Answer
↓
QueryResponse
```

↓

Output:

```json
{
  "answer":"Hemoglobin is within normal range..."
}
```

---

# Swagger Testing

URL:

```text
http://127.0.0.1:8000/docs
```

Tested:

```text
POST /chat
```

---

# Concepts Learned

## FastAPI Endpoint

```python
@app.post("/chat")
```

Used to create chat APIs.

---

## Request Model

Receives user query.

---

## Response Model

Returns structured JSON output.

---

## Component Reusability

Reused existing RAG chatbot component inside FastAPI.

---

## JSON Communication

Input:

JSON

↓

Python Objects

↓

LLM

↓

JSON Response

---

## Separation of Concerns

Separated:

* API Layer
* Components
* Entity Models

---

# Folder Structure

```text
src/
│
├── entity/
│      request_models.py
│
│      response_models.py
│
├── components/
│      rag_chatbot.py
│
├── logger/
│
└── app.py
```

---

# Day 14 Outcome

✅ Real RAG Chat API

✅ FastAPI Integration

✅ FAISS Integration

✅ Llama3 Integration

✅ Swagger Testing

✅ JSON Request & Response

✅ Component Reusability

---

# Current Project Capabilities

### 📄 Medical Report Summarizer

Generate structured medical summaries.

### 💬 Medical Chatbot

Ask questions about the uploaded report.

Powered by:

* FAISS
* Retriever
* Llama3
* FastAPI

---

# Final Architecture

```text
PDF
↓
Extraction
↓
Chunking
↓
Embeddings
↓
FAISS
↓
Retriever
↓
Top K Chunks
↓
Llama3
↓
Answer
↓
FastAPI
↓
JSON Response
```

---

# Git Commands

```bash
git add .

git commit -m "feat: integrate RAG chatbot with FastAPI"

git push origin main
```

---

# Day 14 Status ✅

AI Medical Report Analyzer now supports:

✔ RAG Chatbot

✔ FastAPI Backend

✔ JSON APIs

✔ Swagger Testing

---

# Next

## Day 15

Implement RAG Summary API

```text
GET /summary
↓
RAG Summary Generator
↓
Llama3
↓
JSON Response
```
