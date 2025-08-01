from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

from sklearn.metrics.pairwise import cosine_similarity

import numpy as np


load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large' , dimensions=300)

documents = [

"Asheqeen-Always thoughtful and kind, you bring calm energy wherever you go.",
"Afzal-Your sharp mind and sense of humor make every moment smarter and funnier.",
"Jawad-Loyal to the core, your presence feels like a shield of strength and support.",
"Hamdan-Creative and curious, you're the spark that lights up every conversation.",
"Shahab- Confident and wise, your leadership inspires everyone around you."

]


query = "Tell me about Asheqeen"

doc_embeddings=embedding.embed_documents(documents)
query_embeddings=embedding.embed_query(query)

scores=cosine_similarity([query_embeddings],doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x:x [1])[-1]

print(query)
print(documents[index])
print("Similarity score is :", score)