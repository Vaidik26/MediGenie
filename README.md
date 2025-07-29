# 🧠 MediGenie: RAG-Based Medical Chatbot 💊

MediGenie is a Retrieval-Augmented Generation (RAG) chatbot designed to provide intelligent responses to medical queries. Powered by **Google Gemini 2.5 Flash**, **LangChain**, and **Pinecone**, it combines LLM reasoning with factual retrieval from a local knowledge base (PDF medical book).

---

## 🚀 Features

- ⚡ Fast, factual medical question answering
- 📚 Embeds your own medical knowledge base (PDF)
- 🔍 Uses **Pinecone** for vector search
- 🔗 Built with **LangChain** RAG pipeline
- 🤖 Powered by **Google Gemini-2.5-Flash**
- 🌐 Flask web interface for user interaction

---

## 🗂️ Project Structure

MediGenie/
│
├── data/
│ └── Medical_book.pdf # Source knowledge base
│
├── src/
│ ├── init.py
│ ├── helper.py # Utility functions
│ └── prompt.py # Prompt templates
│
├── templates/
│ └── chat.html # Frontend UI
│
├── static/
│ └── style.css # Optional: Custom styles
│
├── app.py # Flask app with routes
├── store_index.py # Vectorstore creation script
├── requirements.txt # Python dependencies
└── .env # Environment variables

---

## 🧠 RAG Pipeline Overview

1. **Index Creation**: 
   - `store_index.py` uses `PineconeVectorStore.from_documents()` to index PDF chunks.
2. **Retrieval**: 
   - Embeddings are matched with user queries using `Pinecone.from_existing_index`.
3. **Generation**:
   - Retrieved context is passed to Gemini 2.5 Flash via LangChain's `ChatGoogleGenerativeAI`.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/MediGenie.git
cd MediGenie
```
### 2. Create and Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Create a .env file in the project root:

GOOGLE_API_KEY=your_gemini_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=your_pinecone_environment


### 5. Index the Medical Data

```bash
python store_index.py
```

### 6. Run the Application

```bash
python app.py
```

Visit http://127.0.0.1:5000 in your browser.

---

## 💬 Sample Query

User: "What are the symptoms of pneumonia?"
MediGenie: "Common symptoms include cough, fever, chills, and difficulty breathing..."

---

## 📦 Requirements

Python 3.10+

LangChain

Pinecone-client

Flask

google-generativeai

python-dotenv

pdfminer.six

tiktoken or equivalent tokenizer

---

## 📸 UI Preview

✨ Future Improvements

Add memory for follow-up questions

Streamlit interface (optional)

User authentication for hosted version

---

## 🧑‍⚕️ Author

Vaidik Yadav

📫 vaidiky90@gmail.com

