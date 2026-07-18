# 🤖 RAG Chatbot using LangChain, Hugging Face, Pinecone & Groq

A Retrieval-Augmented Generation (RAG) application built with **Python**, **LangChain**, **Hugging Face Embeddings**, **Pinecone**, and **Groq LLM**. The application reads PDF documents, converts them into embeddings, stores them in Pinecone, and answers user questions using Retrieval-Augmented Generation.

---

## 🚀 Features

* Upload and process multiple PDF documents
* Read PDFs using PyPDFLoader
* Split documents into chunks
* Generate embeddings using Hugging Face
* Store embeddings in Pinecone Vector Database
* Retrieve relevant chunks using similarity search
* Generate answers using Groq LLM
* FastAPI endpoint for question answering

---

## 🛠️ Tech Stack

* Python
* FastAPI
* LangChain
* Hugging Face Embeddings
* Pinecone
* Groq
* PyPDF
* Python Dotenv

---

## 📂 Project Structure

```text
rag-project/
│
├── main.py
├── ap.py
├── upload.py
├── query.py
├── requirements.txt
├── .env
│
├── data/
│
└── utils/
    ├── embedding.py
    └── pinecone_db.py
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/faizannasim/RAG-Project.git
```

Move into the project

```bash
cd RAG-Project
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
```

---

## 📄 Upload Documents

Place your PDF files inside the `data` folder.

Run:

```bash
python upload.py
```

This will:

* Read PDF documents
* Split them into chunks
* Generate embeddings
* Store vectors in Pinecone

---

## ▶️ Run the API

```bash
uvicorn main:app --reload
```

API URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## 💬 API Example

### Request

```http
POST /chat
```

```json
{
  "question": "What is Retrieval-Augmented Generation?"
}
```

### Response

```json
{
  "answer": "Retrieval-Augmented Generation (RAG) combines information retrieval with a language model to generate context-aware answers."
}
```

---

## 🔄 RAG Workflow

```text
PDF Documents
      │
      ▼
PyPDFLoader
      │
      ▼
Chunking
      │
      ▼
Hugging Face Embeddings
      │
      ▼
Pinecone Vector Database
      │
      ▼
Similarity Search
      │
      ▼
Retriever
      │
      ▼
Groq LLM
      │
      ▼
Generated Answer
```

---

## 📌 Future Improvements

* React Frontend
* Chat History
* Streaming Responses
* Multiple Vector Databases
* Conversation Memory
* Source Citation
* Docker Support
* Cloud Deployment

---

## 👨‍💻 Author

**Faizan Nasim**

GitHub: https://github.com/faizannasim
