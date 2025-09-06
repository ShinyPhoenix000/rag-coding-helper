from rag.helper import answer_question

def main():
    print("Building vectorstore...")
    print("Vectorstore ready. You can now ask questions!\n")
    while True:
        question = input("Ask a question (or type 'exit' to quit): ")
        if question.lower() == "exit":
            print("Goodbye!")
            break
        answer = answer_question(question, use_mock=True, k=3)
        print("\nAnswer:\n", answer, "\n")

if __name__ == "__main__":
    main()