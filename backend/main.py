from pinecone import init
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from secret_keys import OPENAI_APIKEY, pinecone_apikey, pinecone_environment

test_string = "I have a master's degree in Finance and four years of relevant experience. I am looking for senior level job."

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

# Accept user input
query = test_string

if query:
# Process the input and display the results
    docs = pinecone_vector_store.similarity_search(query=query, k=15)
    sorted_job_list = []
    for doc in docs:
        sorted_job_list.append(doc.page_content)

    print(sorted_job_list)

