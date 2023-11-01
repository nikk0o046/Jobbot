import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
NAV_PUBLIC_API_KEY = os.environ['NAV_PUBLIC_API_KEY']

url = "https://arbeidsplassen.nav.no/public-feed/api/v1/ads"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {NAV_PUBLIC_API_KEY}"  # replace this with your API key
}

max_page_size = 50
desired_number_of_results = 500
total_requests = desired_number_of_results // max_page_size

all_data = []

for page_number in range(total_requests):
    print(f"Fetching page {page_number}...")
    
    # Define the parameters for the request
    params = {
        "size": max_page_size,
        "category": "Bygg og anlegg",  # using the categoryLevel1 for construction jobs
        "pageNumber": page_number
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    all_data.extend(data["content"])
    
    # Check if we've reached the last page of results
    if len(data["content"]) < max_page_size:
        break

# Save all the data
with open('norway_data.json', 'w') as f:
    json.dump(all_data, f)

print(len(all_data))

# Print the first 3 jobs
for job in all_data[:3]:
    print("\nJob Title: ", job['title'])
    print("Employer: ", job['employer']['name'])
    print("Description: ", job['description'])
    print("Content: ", job)
    print("\n" + "-" * 50)  # For readability
