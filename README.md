# RAG-Powered Coding Helper

A Python tool to query API documentation and technical cheat sheets using Retrieval-Augmented Generation (RAG). Ingests Markdown docs, builds a semantic vector store (FAISS), and answers natural language questions with relevant code snippets or explanations.

## Project Structure

```
rag-coding-helper/
├── main.py                # CLI entry point
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore rules
├── data/                  # Markdown docs (API, cheatsheets)
│   ├── pandas.md
│   ├── requests.md
│   ├── ...
├── rag/                   # Core RAG logic
│   ├── helper.py
│   ├── retriever.py
│   ├── llm.py
│   └── __init__.py
├── app/                   # (Optional) App entrypoints
│   └── main.py
├── tests/                 # Unit tests
│   └── test_llm.py
```

## Features

- Ingests Markdown documentation and cheat sheets
- Builds a FAISS vector store for fast semantic search
- Supports HuggingFace, OpenAI, or mock embeddings (offline)
- Natural language question answering with code snippet retrieval
- Extensible: add your own docs to `data/`

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/rag-coding-helper.git
   cd rag-coding-helper
   ```
2. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **(Optional) Set OpenAI API key**
   - For OpenAI embeddings, set your API key:
     ```bash
     export OPENAI_API_KEY=your-key-here
     ```

## Usage Example

Run the CLI and ask a question:

```bash
python main.py
```

**Sample session:**
```
Building vectorstore...
Vectorstore ready. You can now ask questions!

Ask a question (or type 'exit' to quit): How do I create a DataFrame in pandas?

Answer:
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(df)

Ask a question (or type 'exit' to quit): exit
Goodbye!
```

## Configuration

- **Mock Embeddings (default):**
  - Works offline, no API keys needed.
  - Set `use_mock=True` (default in code).
- **HuggingFace Embeddings:**
  - Install `sentence-transformers`.
  - Set `USE_HUGGINGFACE = True` in `rag/retriever.py`.
- **OpenAI Embeddings:**
  - Set `USE_HUGGINGFACE = False` in `rag/retriever.py`.
  - Set your `OPENAI_API_KEY` environment variable.

## Contributing

- Fork the repo and create a feature branch
- Write clear, well-documented code
- Add or update tests in `tests/`
- Submit a pull request with a clear description

## License

MIT License

## References

- [LangChain](https://github.com/langchain-ai/langchain)
- [FAISS](https://github.com/facebookresearch/faiss)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/index)
