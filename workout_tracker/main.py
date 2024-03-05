import random

import requests
import json
from datetime import datetime, timedelta

with open('../config.json') as f:
    config_data = json.load(f)

nutritionix_apikey = config_data["nutritionix"]["API_KEY"]
nutritionix_appid = config_data["nutritionix"]["APP_ID"]

header_para = {
    "Content-Type": "application/json",
    "x-app-id": nutritionix_appid,
    "x-app-key": nutritionix_apikey
}
user_input = input("Tell me which exercises you did: ")
"I ran 1 mile"

data = {
    "query": user_input
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                         headers=header_para, json=data)
response.raise_for_status()
print(response.json)
print(response.text)

sheet_bearer_token = config_data["sheet"]["bearer_token"]
sheet_apikey = config_data["sheet"]["apikey"]

auth_header = {
    "Authorization": sheet_bearer_token
}

sheet_response = requests.get(url=f"https://api.sheety.co/{sheet_apikey}/myWorkouts2024/workouts"
                               , headers=auth_header)
print(sheet_response.text)
