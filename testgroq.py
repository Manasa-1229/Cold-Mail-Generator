import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

groq_api_key = os.getenv("LLM_API_KEY")

# Now you can use the api_key variable
print(groq_api_key) 

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    api_key=groq_api_key,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

response = llm.invoke("Andrew ng is a poineer in ...")
print(response)