import os
import json
from transformers import AutoModel
import torch
from pinecone import init, Index
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
pinecone_apikey = os.environ['pinecone_apikey']
pinecone_environment = os.environ['pinecone_environment']

model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-small-en', trust_remote_code=True)

def get_embedding(text):
    # Convert the text to embeddings using the Jina Embedding model
    with torch.no_grad():  # Ensure you're not computing gradients
        embeddings = model.encode([text])
    # Convert tensor to list for serialization
    return embeddings[0].tolist()

def load_data():
    # Initialize Pinecone
    init(api_key=pinecone_apikey, environment=pinecone_environment)
    
    # Load job listings from the JSON file
    with open('norway_construction_data.json', 'r', encoding='utf-8') as file:
        job_listings = json.load(file)["content"]
    
    # Extract summaries
    summaries = [job['summary'] for job in job_listings if 'summary' in job]
    
    # Create embeddings for each summary
    vectors = []
    for idx, (summary, job_listing) in enumerate(zip(summaries, job_listings)):
        embedding = get_embedding(summary)
        vectors.append({
            'id': job_listing['uuid'],  # using UUID as the unique ID for each vector
            'values': embedding
        })
        print(f"Processed {idx + 1}/{len(summaries)} embeddings.")
    
    # Use Pinecone's upsert to add data
    index = Index("jobbotindex")
    upsert_response = index.upsert(vectors)
    
    print(upsert_response)

# Load the data
load_data()

