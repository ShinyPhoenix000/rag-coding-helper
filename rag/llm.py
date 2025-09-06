from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from pathlib import Path

def get_rag_chain(vectorstore_path: str = None):
    vectorstore_path = Path(vectorstore_path or Path(__file__).parent.parent / "vectorstore")
    vectorstore = FAISS.load_local(str(vectorstore_path))
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0),
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    return qa_chain

if __name__ == "__main__":
    qa = get_rag_chain()
    query = "How do I send an email using Python's Gmail API?"
    print(qa.run(query))