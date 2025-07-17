# app.py

import streamlit as st
from rag_helper import process_pdfs, create_qa_chain
import os

st.set_page_config(page_title="RAG PDF Chatbot", layout="centered")
st.title("📄 RAG-powered PDF Chatbot using Ollama")

# Ensure the 'pdfs' directory exists
pdf_directory = "pdfs"
os.makedirs(pdf_directory, exist_ok=True)

uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        with open(os.path.join(pdf_directory, file.name), "wb") as f:
            f.write(file.read())
    st.success("PDFs uploaded successfully!")

if st.button("🧠 Process PDFs"):
    with st.spinner("Processing..."):
        vectorstore = process_pdfs(pdf_directory)
        qa_chain = create_qa_chain(vectorstore)
        st.session_state.qa_chain = qa_chain
    st.success("Vector store and QA system created!")

if "qa_chain" in st.session_state:
    question = st.text_input("Ask a question about your PDFs:")
    if question:
        with st.spinner("Thinking..."):
            result = st.session_state.qa_chain({"query": question})
            st.success("Answer:")
            st.write(result["result"])
