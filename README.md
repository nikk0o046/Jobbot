## Jobbot - Introduction

This project is a web application that uses machine learning and natural language processing to find most relevant job listings to a user.

This application allows users to input description of their education, experience and skills. This description is used to show users most relevant job listings. These job listings are translated and summarized job listings for construction industry pulled from a Norwegian public job portal. Users are shown these listings one-by-one and they deside to like, dislike or superlike them. Liked and superliked job listings are stored to Likes -page to apply later.

Video clip about the app in use here:
https://clipchamp.com/watch/qkRv6uozMaV

## Features and Workflow:

**Data Collection:** Fetched job listings specifically from a Norwegian public job portal, focusing on the construction industry. I focused on one industry, because I wanted to limit the amount of job listings but still make it challenging for the model to decide between listings to show. It would be easier for the model to decide between a banking job and a cleaning job than with two jobs from the same industry.

**Translation and Summarization:** Utilized GPT-3.5-turbo in conjunction with Langchain to translate and create concise summaries of the original job listings.

**Advanced Indexing:** The translated and summarized job listings were converted into word embeddings and indexed in Pinecone, a vector database. The 'BAAI/bge-large-zh-v1.5' model from the transformers library was chosen for this process due to its optimal retrieval performance on the MTEB benchmark.

**User-Centered Search:** When a user inputs their description, it's also converted into a word embedding. Pinecone then performs a cosine similarity search to retrieve the most semantically similar job summaries.

**Interactive Frontend Display:** The retrieved job summaries are sorted and sent to the frontend, where users can view and interact with them one by one.

## Technologies

Frontend: React, Vite, React-router, Material-ui, Node.js, Npm
Backend: Pytorch, Pinecone, Flask & flask_cors, Langchain/OpenAI, Transformers

## Setting Up and Testing the Jobbot Application

**Prerequisites:**
Python 3.x
A virtual environment tool like venv.
Necessary API keys for OpenAI, Pinecone, NAV Public, and HuggingFace.

**Install Dependencies**

pip install -r requirements.txt

**Environment Variables**
Set up your environment variables. NAV_PUBLIC_API_KEY is not needed, if you don't fetch any new data.

OPENAI_API_KEY: The API key for accessing OpenAI's GPT-3.5-turbo services.
pinecone_apikey: The API key required to interact with the Pinecone vector database.
pinecone_environment: Specifies the environment for the Pinecone service.
NAV_PUBLIC_API_KEY: The API key used for accessing the Norwegian public job portal. You can get it here: https://github.com/navikt/pam-public-feed/
HUGGINGFACE_API_TOKEN: Token for accessing models and other resources from the HuggingFace Hub.

OPENAI_API_KEY=[YOUR_OPENAI_API_KEY]
pinecone_apikey=[YOUR_PINECONE_API_KEY]
pinecone_environment=[YOUR_PINECONE_ENVIRONMENT]
NAV_PUBLIC_API_KEY=[YOUR_NAV_PUBLIC_API_KEY]
HUGGINGFACE_API_TOKEN=[YOUR_HUGGINGFACE_API_TOKEN]

**Pinecone**
Create an index on Pinecone's site with 1024 as vector dimensions.

Populate the database:
python populate_database.py

**Run the Backend**
python main.py

**Accessing the Frontend**
Navigate to the frontend directory, install necessary dependencies with npm install, and then use command "npm run dev".

**Use**

- Input your education, experience, and skills. Click "Submit".
- Interact with job listings as desired

**Fetching new data**
If you want to fetch new data, get the API key and run:
python norway_fetch_data.py

Then, I decided to remove listings if their employer name and job title were identical:
python duplicate_finder.py

After that, create summaries:
python create_summaries.py

Now you are ready to populate the database with new data and proceed as already told above.

# Contact info

nikk0o046@gmail.com
