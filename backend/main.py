import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from pinecone import init, Index
from dotenv import load_dotenv
from populate_database import get_embedding  # Importing the function from your module

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

# Load environment variables
load_dotenv()
pinecone_apikey = os.environ['pinecone_apikey']
pinecone_environment = os.environ['pinecone_environment']

# Initialize Pinecone
init(api_key=pinecone_apikey, environment=pinecone_environment)

# Load job listings from the JSON file
with open('norway_construction_data_no_duplicates.json', 'r', encoding='utf-8') as file:
    job_listings = json.load(file)["content"]

# Create a mapping from UUIDs to job listings
job_dict = {job["uuid"]: job for job in job_listings}

# Create a Pinecone index instance
index = Index("jobbotindex")


@app.route('/function-jobbot', methods=['POST'])
def search_jobs():
    data = request.json
    input_string = data.get('input_string')

    if not input_string:
        return jsonify({"error": "input_string is required!"}), 400

    # Convert the query to embeddings using the get_embedding function
    query_embedding = get_embedding(input_string)
    
    # Process the input and fetch relevant job listings
    docs = index.query(queries=[query_embedding], top_k=15)
    # Turn returned UUIDs into a list of job summaries which the frontend expects
    job_summaries = [job_dict[doc.id]['summary'] for doc in docs.results[0].matches]

    return jsonify(job_summaries), 200

# Run the app on default port 5000
if __name__ == '__main__':
    app.run(debug=True)
