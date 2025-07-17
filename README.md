# 🤖 RAG-powered PDF Chatbot with Ollama and Streamlit

This is a lightweight local chatbot that lets you upload PDFs and ask questions about them using Retrieval-Augmented Generation (RAG). It uses:

- 🧠 [Ollama](https://ollama.com/) for running open-source LLMs locally
- 📄 LangChain for document processing & QA chains
- 🔍 FAISS as a vector store for fast document search
- 📊 Streamlit as the user interface

---

## 💡 What You Can Do

- Upload PDFs
- Ask questions about the content
- Get answers powered by local LLMs (no API required!)
- All processing is done locally

---


# rag_ollama_pdf_streamlit


## ⚙️ Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/your-username/rag_pdf_app.git
cd rag_pdf_app
```
#Create a virtual environment (optional but recommended)

python -m venv venv
source venv/Scripts/activate  # For Windows
# OR
source venv/bin/activate      # For Linux/Mac

#Install dependencies

pip install -r requirements.txt

# Run the app
streamlit run app.py

Made with ❤️ by Deepu Kumar

### ✅ Next Steps:

- Save this as `README.md` in your repo.
- Also create a `.gitignore` file (if you haven’t already).

Let me know if you want me to also create the `requirements.txt` file for you.
