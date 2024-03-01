import requests
import json

with open('../config.json') as f:
    config_data = json.load(f)

# Access database configuration
pixela_token = config_data["pixela"]["token"]
pixela_username = config_data["pixela"]["username"]
user_info = {"token": pixela_token,
             "username": pixela_username,
             "agreeTermsOfService": "yes",
             "notMinor": "yes"
             }

response = requests.post(url="https://pixe.la/v1/users", json=user_info)
print(response.text)
