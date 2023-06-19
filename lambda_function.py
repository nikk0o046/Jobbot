import os
import json
from pinecone import init
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings

def lambda_handler(event, context):
    # Extract the query from the HTTP POST body
    body = json.loads(event.get('body', {}))
    query = body.get('query', '')

    # Get API keys from environment variables
    OPENAI_APIKEY = os.getenv('OPENAI_APIKEY')
    pinecone_apikey = os.getenv('PINECONE_APIKEY')
    pinecone_environment = os.getenv('PINECONE_ENVIRONMENT')

    # Initialize Pinecone
    init(
        api_key=pinecone_apikey,
        environment=pinecone_environment
    )
    index_name = "jobbotindex"
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_APIKEY)

    pinecone_vector_store = Pinecone.from_existing_index(
        index_name=index_name,
        embedding=embeddings
    )

    # Process the input and display the results
    if query:
        docs = pinecone_vector_store.similarity_search(query=query, k=15)
        sorted_job_list = []
        for doc in docs:
            sorted_job_list.append(doc.page_content)

        # Return the job list as the response
        return {
            'statusCode': 200,
            'body': json.dumps(sorted_job_list),
            'headers': {
                'Content-Type': 'application/json',
            },
        }

    # If there was no query, return an error message
    else:
        return {
            'statusCode': 400,
            'body': 'No query provided',
        }
