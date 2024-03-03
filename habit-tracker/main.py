import requests
import json
from datetime import datetime, timedelta

with open('../config.json') as f:
    config_data = json.load(f)
GRAPH_NAME = "code-graph"

pixela_token = config_data["pixela"]["token"]
pixela_username = config_data["pixela"]["username"]


def pixel_create_user(username: str, token: str):
    user_info = {"token": token,
                 "username": username,
                 "agreeTermsOfService": "yes",
                 "notMinor": "yes"
                 }
    response = requests.post(url="https://pixe.la/v1/users", json=user_info)
    print(response.text)


pixel_create_user(pixela_username, pixela_token)
headers = {
    "X-USER-TOKEN": pixela_token
}


def pixel_create_graph(username, graph_name, unit, unit_type):
    graph_endpoint = f"https://pixe.la/v1/users/{username}/graphs"
    print(graph_endpoint)
    graph_config = {
        "id": "code-graph",
        "name": graph_name,
        "unit": unit,
        "type": unit_type,
        "color": "shibafu"
    }
    graph_response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
    print(graph_response)


pixel_create_graph(pixela_username, GRAPH_NAME, "hours", "int")


def graph_pixel_add(day: str, qty: int):
    add_endpoint = f"https://pixe.la/v1/users/{pixela_username}/graphs/{GRAPH_NAME}"
    graph_pixel_config = {
        "date": day,
        "quantity": str(qty),
    }
    graph_pixel_response = requests.post(url=add_endpoint, headers=headers, json=graph_pixel_config)
    print(graph_pixel_response.text)


def graph_pixel_update(day: str, qty: int):
    update_endpoint = f"https://pixe.la/v1/users/{pixela_username}/graphs/{GRAPH_NAME}/{day}"
    graph_pixel_config = {
        "quantity": str(qty),
    }
    graph_pixel_response = requests.put(url=update_endpoint, headers=headers, json=graph_pixel_config)
    print(graph_pixel_response.text)


def graph_pixel_delete(day: str):
    delete_endpoint = f"https://pixe.la/v1/users/{pixela_username}/graphs/{GRAPH_NAME}/{day}"
    graph_pixel_response = requests.delete(url=delete_endpoint, headers=headers)
    print(graph_pixel_response.text)


today = datetime.now().strftime("%Y%m%d")
graph_pixel_add(today, 5)
yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
graph_pixel_add(yesterday, 10)
graph_pixel_update(yesterday, 2)
graph_pixel_delete(yesterday)
