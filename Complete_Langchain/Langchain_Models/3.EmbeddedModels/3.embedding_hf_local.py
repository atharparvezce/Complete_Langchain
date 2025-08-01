from langchain_huggingface import HuggingFaceEmbeddings


embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [

            "Delhi is the capital of India ", 
            "Kolkata is the capital of West Bangal",
            "Lucknow is the capital of Uttar Pradesh",
            "Chandigarh is the capital of Punjab"
    
]

vector = embedding.embed_documents(documents)
  
print(str(vector))