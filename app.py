from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate


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
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", """
        You are an AI Instructor.
        Rules:
        -If you are not confident, say you don't know.
        - Never guess company names, people, or products.
        - Ask for clarification when needed.
        - Do not invent information.
        - If the answer requires external knowledge you don't have, clearly state that.
        -Explain in simple english.
        -give one real world example.
        keep answer short and concise. 
    """),
    ("human", """
    Explain:{topic}
    Format:
    1. Definition
    2. Example
    3. Interview Question
    4. Practice Exercise
    """),
])
# prompt_template = PromptTemplate.from_template(
# """Explain:{topic}

# Format:
# 1. Definition
# 2. Example
# 3. Interview Question
# 4. Practice Exercise
# """)
# chat_history = [
#     # SystemMessage(
#     #     content="""You are an AI Instructor.
#     #     Rules:
#     #     -If you are not confident, say you don't know.
#     #     - Never guess company names, people, or products.
#     #     - Ask for clarification when needed.
#     #     - Do not invent information.
#     #     - If the answer requires external knowledge you don't have, clearly state that.
#     #     -Explain in simple english.
#     #     -give one real world example.
#     #     keep answer short and concise.
#     #     """
#     # )
#     # chat_prompt 
# ]

while True:
    user_query = input("How I can Help you?").strip()
    if user_query.lower() in ["exit", "quit"]:
        print("Exiting the chat. GoodBye!")
        break
    
    if not user_query:
        print("No query provided.")
        continue
    messages = chat_prompt.invoke({"topic": user_query})
    # chat_history.append(formatted_prompt)
    response = llm.invoke(messages)
    # chat_history.append(content=response.content)
    print("\nAssistant:\n")
    print(response.content)

    print()
