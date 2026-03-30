#!/usr/bin/env python3
# pip install -qU langchain langchain-huggingface sentence-transformers
# Run the above command in terminal before executing this script

from langchain_huggingface import HuggingFaceEmbeddings

# Specify the model you want to use
model_name = "sentence-transformers/all-MiniLM-l6-v2"

# Initialize the embeddings object
embeddings = HuggingFaceEmbeddings(model_name=model_name)

print(embeddings)
# Example text to embed
text = "This is a document we want to embed."
query_result = embeddings.embed_query(text)
print(query_result)