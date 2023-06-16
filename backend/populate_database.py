from pinecone import init
from job_test_data import job_data
from secret_keys import OPENAI_APIKEY, pinecone_apikey, pinecone_environment
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings

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