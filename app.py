from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

import os
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Groq API key not found in .env")

# print(api_key)
# user_query = input("Ask me anything: ").strip()

# if not user_query:
#     print("No query provided.")
#     exit()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=api_key
)

chat_history = []

while True:
    user_query = input("How I can Help you?").strip()
    if not user_query:
        print("No query provided.")
        continue

    if user_query.lower() in ["exit", "quit"]:
        print("Exiting the chat. GoodBye!")
        break
    chat_history.append(HumanMessage(content=user_query))
    response = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(response.content)
