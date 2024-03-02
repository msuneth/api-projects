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

graph_endpoint = f"https://pixe.la/v1/users/{pixela_username}/graphs"
headers = {
    "X-USER-TOKEN": pixela_token
}
graph_config = {
    "id":"code-graph",
    "name":"code-graph",
    "unit":"hours",
    "type":"int",
    "color":"shibafu"
}
graph_response = requests.post(url=graph_endpoint,headers=headers,json=graph_config)
print(graph_response.text)