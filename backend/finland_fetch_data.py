import requests
from secret_keys import *

token_url = 'https://tedigib2c.b2clogin.com/tedigib2c.onmicrosoft.com/B2C_1A_SIGNIN/oauth2/v2.0/token'
api_url = 'https://integraatiot.tyomarkkinatori.fi/jobpostingprovider/v1/tyopaikat?sivu=0&maara=100'

# parameters for getting the token
token_data = {
    "client_id": finland_client_id,
    "scope": "https://tedigib2c.onmicrosoft.com/fad9328b-e852-45e4-951b6d142430e89d/.default",
    "client_secret": finland_client_secret,
    "response_type": "token",
    "grant_type": "client_credentials"
}

try:
    # get the token
    print(f"Sent POST request to {token_url} with data: {token_data}")
    response = requests.post(token_url, data=token_data)
    response.raise_for_status()  # This will raise an exception if the response contains an HTTP error
    
    token = response.json().get('access_token')
    
    if token:
        print(f"Successfully obtained access token: {token[:15]}...")  # print the first 15 characters for validation without exposing the whole token
        headers = {"Authorization": "Bearer " + token}
        
        # make the GET request
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # raise exception for HTTP errors

        print("API Response:")
        print(response.json())
    else:
        print(f"Failed to retrieve token. Server responded with: {response.json()}")

except requests.exceptions.RequestException as e:  # Catch all HTTP request errors
    print(f"HTTP Request failed: {str(e)}")
    print(response.content)
