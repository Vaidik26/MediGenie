from dotenv import load_dotenv
import os
from src.helper import load_pdf_file, filter_docs, text_split, embedder
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
import warnings

warnings.filterwarnings("ignore")

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

extracted_data = load_pdf_file(data_path="data/")
filter_data = filter_docs(extracted_data)
text_chunks = text_split(filter_data)

embeddings = embedder()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index_name = "medigenie"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

index = pc.Index(index_name)

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings
)