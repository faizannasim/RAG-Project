#from upload import vector
from query import ask_question

print("========== RAG Chatbot ==========")

while True:
    question = input("\nAsk Question: ")
    if question.lower() == "exit":
        break
    answer = ask_question(question)

    print("\nAnswer:\n")

    print(answer)