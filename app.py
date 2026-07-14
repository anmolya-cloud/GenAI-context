from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

prompt = ChatPromptTemplate.from_template(
    "Translate the following text into Hindi :\n\n{topic} in simple words."

)

chain = prompt | llm 

response = chain.invoke({
    "topic": "vector databases"
})

print(response.content)