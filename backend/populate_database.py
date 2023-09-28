from pinecone import init
from job_test_data import job_data
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()
pinecone_apikey = os.environ['pinecone_apikey']
pinecone_environment = os.environ['pinecone_environment']
OPENAI_APIKEY = os.environ['OPENAI_APIKEY']

def load_data():
    # Initialize Pinecone
    init(
        api_key=pinecone_apikey,
        environment=pinecone_environment
    )
    index_name = "jobbotindex"

    # Create embeddings and add texts to the Pinecone index
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_APIKEY)
    Pinecone.from_texts(job_data, embeddings, index_name=index_name)

# Load the data
load_data()