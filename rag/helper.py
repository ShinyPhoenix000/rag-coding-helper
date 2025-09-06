from rag.retriever import get_vectorstore
from langchain.text_splitter import CharacterTextSplitter
from typing import List
import re

def answer_question(query: str, use_mock: bool = True, k: int = 3):
    vectorstore = get_vectorstore(use_mock=use_mock)
    docs = vectorstore.similarity_search(query, k=k)
    if not docs:
        return "No relevant information found."
    splitter = CharacterTextSplitter(separator="\n", chunk_size=150, chunk_overlap=20)
    all_sentences = []
    for doc in docs:
        sentences = splitter.split_text(doc.page_content)
        all_sentences.extend(sentences)
    keyword_weights = {
        "pandas": 3,
        "git": 2,
        "numpy": 3,
    }
    query_keywords = set(re.findall(r'\w+', query.lower()))
    def sentence_score(sentence):
        if use_mock:
            sentence_words = set(re.findall(r'\w+', sentence.lower()))
            semantic_val = sum(weight for kw, weight in keyword_weights.items() if kw in sentence_words)
        else:
            semantic_score = vectorstore.similarity_search(sentence, k=1)
            semantic_val = 1 if semantic_score else 0
        keyword_score = len(query_keywords & set(re.findall(r'\w+', sentence.lower())))
        return semantic_val + keyword_score
    scored_sentences = [(sentence, sentence_score(sentence)) for sentence in all_sentences]
    scored_sentences.sort(key=lambda x: x[1], reverse=True)
    top_sentences = [s for s, _ in scored_sentences[:k]]
    return "\n".join(top_sentences)