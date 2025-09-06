import os
from typing import List
from glob import glob
from langchain.docstore.document import Document

try:
    from langchain_community.vectorstores import FAISS
except ImportError:
    from langchain.vectorstores import FAISS

from langchain.text_splitter import RecursiveCharacterTextSplitter

USE_HUGGINGFACE = True
USE_MOCK = False

if USE_HUGGINGFACE:
    from sentence_transformers import SentenceTransformer
else:
    from langchain_community.embeddings.openai import OpenAIEmbeddings

vectorstore_instance = None

def load_documents(data_folder: str) -> List[Document]:
    all_docs = []
    for file_path in glob(f"{data_folder}/*.md"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
        all_docs.append(Document(page_content=text, metadata={"source": file_path}))
    return all_docs

def build_vectorstore(data_folder: str = "data", use_mock: bool = True):
    all_docs = load_documents(data_folder)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(all_docs)
    if use_mock or USE_MOCK:
        class MockEmbeddings:
            def embed_documents(self, texts):
                vectors = []
                for text in texts:
                    if "pandas" in text.lower():
                        vectors.append([100.0]*768)
                    elif "git" in text.lower():
                        vectors.append([1.0]*768)
                    elif "numpy" in text.lower():
                        vectors.append([50.0]*768)
                    else:
                        vectors.append([0.0]*768)
                return vectors
            def __call__(self, text):
                if "pandas" in text.lower():
                    return [100.0]*768
                elif "git" in text.lower():
                    return [1.0]*768
                elif "numpy" in text.lower():
                    return [50.0]*768
                else:
                    return [0.0]*768
        embeddings = MockEmbeddings()
    elif USE_HUGGINGFACE:
        model = SentenceTransformer("all-MiniLM-L6-v2")
        class HFEmbeddings:
            def embed_documents(self, texts):
                return model.encode(texts).tolist()
            def __call__(self, text):
                return model.encode([text])[0].tolist()
        embeddings = HFEmbeddings()
    else:
        openai_api_key = os.environ.get("OPENAI_API_KEY")
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore

def get_vectorstore(use_mock: bool = True):
    global vectorstore_instance
    if vectorstore_instance is None:
        vectorstore_instance = build_vectorstore(use_mock=use_mock)
    return vectorstore_instance