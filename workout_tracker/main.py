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
                         headers=header_para,json=data)
response.raise_for_status()
print(response.json)
print(response.text)