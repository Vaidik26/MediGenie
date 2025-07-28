from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import List
from langchain.schema import Document
import torch

# Loading pdf data

def load_pdf_file(data_path):
    loader = DirectoryLoader(data_path,
                glob="*.pdf",
                loader_cls=PyPDFLoader)
    
    documents = loader.load()
    
    return documents

# On giving a list of documents return a new list of Document object containing only source and page_content

def filter_docs(docs: List[Document]) -> List[Document]:
    min_docs : List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source")
        min_docs.append(
            Document(
                page_content=doc.page_content,
                metadata = {"source":src}
            )
        )
    return min_docs

# Split the data into text chunks

def text_split(data):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = splitter.split_documents(data)
    return text_chunks

# Download the Embeddings from the HuggingFace

def embedder():
    model = "BAAI/bge-small-en-v1.5"
    embeddings = HuggingFaceEmbeddings(model_name = model)
    return embeddings