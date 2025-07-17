# rag_helper.py

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
import os

def process_pdfs(pdf_folder_path):
    documents = []
    for filename in os.listdir(pdf_folder_path):
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(pdf_folder_path, filename))
            documents.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    chunks = text_splitter.split_documents(documents)

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    return vectorstore

def create_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever()

    llm = Ollama(model="llama3")  # or any other available model in your Ollama setup

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain
