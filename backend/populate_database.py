import os
import json
from transformers import AutoTokenizer, AutoModel
import torch
from pinecone import init, Index
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
pinecone_apikey = os.environ['pinecone_apikey']
pinecone_environment = os.environ['pinecone_environment']

# Load model and tokenizer from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('BAAI/bge-large-en-v1.5')
model = AutoModel.from_pretrained('BAAI/bge-large-en-v1.5')
model.eval()

def get_embedding(text):
    # Tokenize and encode the text using the tokenizer
    encoded_input = tokenizer(text, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        # Pass the tokenized text through the model
        output = model(**encoded_input)
        # Select the last hidden state of the first token (i.e., [CLS]) as the sentence embedding
        embeddings = output.last_hidden_state[:, 0, :].squeeze().tolist()
    return embeddings

def load_data():
    # Initialize Pinecone
    init(api_key=pinecone_apikey, environment=pinecone_environment)
    
    # Load job listings from the JSON file
    with open('norway_construction_data_no_duplicates.json', 'r', encoding='utf-8') as file:
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
if __name__ == '__main__':
    load_data()
