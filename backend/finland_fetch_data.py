import requests
from secret_keys import *

token_url = 'https://tedigidevb2c.b2clogin.com/tedigidevb2c.onmicrosoft.com/B2C_1A_SIGNIN/oauth2/v2.0/token'
api_url = 'https://integraatiot-qa.tyomarkkinatori.fi/'

# parameters for getting the token
token_data = {
    "client_id": finland_client_id,
    "scope": 'https://tedigidevb2c.onmicrosoft.com/07fd933a-dd1b-4c6d-8eee-ffedf3fbb3da/.default',
    "client_secret": finland_client_secret,
    "grant_type": "client_credentials"
}

# get the token
response = requests.post(token_url, data=token_data)
token = response.json().get('access_token')
print(token)

if token:
    # use the token to authenticate your GET request
    headers = {"Authorization": "Bearer " + token}

    # make the GET request
    response = requests.get(api_url, headers=headers)
    print(response.json())
else:
     print(f"Failed to retrieve token. Server responded with: {response.json()}")
