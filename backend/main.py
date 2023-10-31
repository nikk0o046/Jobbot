import os
import torch
from transformers import AutoModel
from pinecone import init, Index
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
pinecone_apikey = os.environ['pinecone_apikey']
pinecone_environment = os.environ['pinecone_environment']

test_string = """Experience: 3 years as an electrician
Education: Electrician
Skills: """

# Load the Jina model
model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-small-en', trust_remote_code=True)

def get_embedding(text):
    """Generate embeddings using Jina model."""
    with torch.no_grad():
        embeddings = model.encode([text])
    return embeddings[0].tolist()

# Initialize Pinecone
init(
    api_key=pinecone_apikey,
    environment=pinecone_environment
)
index_name = "jobbotindex"

# Load the job listings
with open('norway_construction_data.json', 'r', encoding='utf-8') as file:
    job_listings = json.load(file)["content"]

# Create a mapping from UUIDs to job listings
job_dict = {job["uuid"]: job for job in job_listings}

# Create a Pinecone index instance
index = Index(index_name)

# Accept user input
query = test_string

if query:
    # Convert the query to embeddings using the Jina model
    query_embedding = get_embedding(query)
    
    # Process the input and display the results
    docs = index.query(queries=[query_embedding], top_k=15)
    sorted_job_list = [job_dict[doc.id] for doc in docs.results[0].matches]

    print("NEW QUERY!!!!!!!!!!!!!!!!!!!!!")
    for item in sorted_job_list:
        print(f"Job uuid: {item['uuid']}")
        print(item['summary'], '\n')
        print("---------------------------------")

