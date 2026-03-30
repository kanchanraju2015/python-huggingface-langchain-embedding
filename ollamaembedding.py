# first run ollama run llama3.2:1b
# ollama list 
# ollama pull <modelname>
# ollama run <modelname>
# check http://localhost:11434 for ollama running or not 
 
from langchain_community.embeddings import OllamaEmbeddings


embeddings=OllamaEmbeddings(model="gemma:2b")

text="what is artificial intelligence"

embed_vector=embeddings.embed_query(text)# use embed_documents for document embedding 

print(embed_vector)  # prints the embeddings 

print(len(embed_vector)) # prints the length of embedding

