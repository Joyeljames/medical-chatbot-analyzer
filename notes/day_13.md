# Day 17 – Dynamic Vector Store Reload

## Objective

Enable the chatbot and summary endpoints to work with newly uploaded PDFs without restarting FastAPI.

---

# Problem

Initially, the vector store and retriever were loaded only once when FastAPI started.

```text
Server Start
↓
Load FAISS
↓
Create Retriever
↓
Upload New PDF
↓
Create New FAISS
↓
Chatbot still uses old retriever ❌
```

As a result, `/chat` and `/summary` returned information from the previous PDF.

---

# Solution

After uploading a new PDF:

1. Extract text
2. Create chunks
3. Generate embeddings
4. Create new FAISS database
5. Reload chatbot retriever
6. Reload summary retriever

```text
Upload PDF
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
FAISS
↓
Reload Retriever
↓
Chat and Summary use latest PDF ✅
```

---

# Upload Endpoint

```python
@app.post("/upload")
def upload_pdf(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    text = pdf_load.extract_text(file_path)

    chunks = chunkng.create_chunks(text)

    vectore_store.create_vectore_store(chunks)

    chatbot.reload_vectorstore()

    summary_generator.reload_vectores()

    return {
        "message": "PDF processed completed"
    }
```

---

# Reload Vector Store

```python
def reload_vectorstore(self):

    self.vector_store = vector.load_vectore()

    self.retriever = self.vector_store.as_retriever(
        search_kwargs={"k": 3}
    )
```

---

# Why Reload?

Without reloading:

```text
Retriever
↓
Old PDF
```

After reloading:

```text
Retriever
↓
Latest Uploaded PDF
```

---

# Summary Endpoint

```python
docs = summary_generator.retriever.invoke(
    "Summarize this medical report"
)

context = "\n".join(
    [doc.page_content for doc in docs]
)

summary_response = summary_generator.generate_summary(
    context=context
)
```

---

# Components Used

### PdfLoader

Extract text from PDF.

### textchunk

Split text into chunks.

### vectorstoreManager

Create and load FAISS vector database.

### RagChatBot

Answer user queries using RAG.

### RagSummarizer

Generate report summaries.

---

# Current API Endpoints

### Home

```http
GET /
```

### Upload PDF

```http
POST /upload
```

### Chat

```http
POST /chat
```

### Summary

```http
GET /summary
```

---

# Flow Diagram

```text
User Uploads PDF
↓
PDF Loader
↓
Chunking
↓
Embeddings
↓
FAISS Database
↓
Reload Retriever
↓
Chat Endpoint
↓
Summary Endpoint
```

---

# Features Completed

* PDF Upload
* Text Extraction
* Chunking
* Embeddings
* FAISS Vector Store
* Retriever
* Chatbot
* Summary Generator
* Dynamic Vector Store Reload
* No Server Restart Required

---

# Key Learning

Retrievers are created from vector stores.

When a new PDF creates a new FAISS database, the retriever must also be recreated.

```python
self.retriever = self.vector_store.as_retriever()
```

Otherwise, the chatbot continues using the old retriever.

---

# Git Commands

```bash
git add .

git commit -m "feat: add dynamic vector store reload after PDF upload"

git push origin main
```

---

# Day 17 Outcome

Successfully built a dynamic AI Medical Report Analyzer capable of processing multiple PDFs and updating chatbot and summary responses automatically without restarting FastAPI.
