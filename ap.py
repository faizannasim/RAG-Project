# #from upload import vector
# from query import ask_question

# print("========== RAG Chatbot ==========")
# count = 1

# while True:
#     question = input(f"\nQuestion {count}: ")
#     if question.lower() == "exit":
#         break
#     #answer = ask_question(question)

    
#     print("\nAnswer:\n",flush=True)
#     #print(answer)
#     ask_question(question)
#     count += 1
#     # print(answer)
   

from query import ask_question

print("========== RAG Chatbot ==========")

count = 1

while True:
    question = input(f"\nQuestion {count}: ")

    if question.lower().strip() == "exit":
        break

   
    print("\nAnswer:", flush=True)
    ask_question(question)


    count += 1




