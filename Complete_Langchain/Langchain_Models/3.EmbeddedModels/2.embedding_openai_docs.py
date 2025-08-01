from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = [

            "Delhi is the capital of India ", 
            "Kolkata is the capital of West Bangal",
            "Lucknow is the capital of Uttar Pradesh",
            "Chandigarh is the capital of Punjab"
    
]

result = embedding.embed_documents(documents)

print(str(result))