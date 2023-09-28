def process_string(request):
    from flask import jsonify
    import os
    from pinecone import init
    from langchain.vectorstores import Pinecone
    from langchain.embeddings.openai import OpenAIEmbeddings

    # Get API keys from environment variables
    OPENAI_APIKEY = os.getenv('OPENAI_APIKEY')
    pinecone_apikey = os.getenv('PINECONE_APIKEY')
    pinecone_environment = os.getenv('PINECONE_ENVIRONMENT')

    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows POST requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return '', 204, headers

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'input_string' in request_json:
        query = request_json['input_string']
        
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

        docs = pinecone_vector_store.similarity_search(query=query, k=15)

        sorted_job_list = []
        for doc in docs:
            sorted_job_list.append(doc.page_content)

        return jsonify(sorted_job_list), 200, headers
    else:
        return 'Missing "input_string" in request', 400, headers