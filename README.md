## Jobbot

This project is a web application that uses machine learning and natural language processing to find most relevant job listings to a user.

This application allows users to input description of their education, experience and skills. This description is used to show users most relevant job listings. These job listings are translated and summarized job listings for construction industry pulled from a Norwegian public job portal. Users are shown these listings one-by-one and they deside to like, dislike or superlike them. Liked and superliked job listings are stored to Likes -page to apply later.

Video clip about the app in use here:
https://clipchamp.com/watch/qkRv6uozMaV

How it works:
First, I fetched a bunch of job listings from a Norwegian public job portal for construction industry. I focused on one industry, because I wanted to limit the amount of job listings but still make it difficult for the model to decide between fitting jobs. I used GPT-3.5-turbo with Langchain to create translated summaries.

Summarized job listings are indexed and stored as word embeddings in a vector database (Pinecone), using 'BAAI/bge-large-zh-v1.5' model from transformers library. User's description is also embedded, after which Pinecone performs cosine similary search to find most semantically similar job summaries. These job summaries are sent to the frontend as a sorted list, which are shown to the useron by one.

# Technologies

Frontend

- React
- Vite
- React-router
- Material-ui
- Node
- Npm

Backend

- Pytorch
- Pinecone : To store and query vectors
- Flask & flask_cors : For backend app
- Langchain / OpenAI : To create translated summaries of job listings
- Transformers : For embedding models. I ended up using 'BAAI/bge-large-zh-v1.5' as it had the best retriaval performance on the MTEB benchmark, and it's sequence length was long enough for all of my summaries. It also performed much better than 'jinaai/jina-embeddings-v2-small-en', which would have been much smaller in size.
- Huggingface(?) : I used embedding models from huggingface, but through transformers library

# Contact info

nikk0o046@gmail.com
