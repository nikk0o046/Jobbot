from secret_keys import *
import requests
import json
import os

url = "https://arbeidsplassen.nav.no/public-feed/api/v1/ads"

headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {NAV_PUBLIC_API_KEY}"  # replace this with your actual API key
}

response = requests.get(url, headers=headers)

# if file does not exist, make request and save the data
if not os.path.exists('norway_data.json'):
    response = requests.get(url, headers=headers)
    data = response.json()  # use requests' built-in JSON decoder

    with open('norway_data.json', 'w') as f:
        json.dump(data, f)
# if file exists, load the data
else:
    with open('norway_data.json', 'r') as f:
        data = json.load(f)

# Now, you can access fields from the data
print(data["totalElements"])

# Let's print the first 5 job listings

for job in data['content'][:3]:
    print("\nJob Title: ", job['title'])
    print("Employer: ", job['employer']['name'])
    print("Description: ", job['description'])
    print("Content: ", job)
    print("\n" + "-" * 50) # For readability