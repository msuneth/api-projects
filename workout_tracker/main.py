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
user_input = input("Tell me which exercises you did with duration: ")

data = {
    "query": user_input
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                         headers=header_para, json=data)
response.raise_for_status()
response_data = response.json()
workout_name = response_data["exercises"][0]["name"]
workout_duration = response_data["exercises"][0]["duration_min"]
workout_calories = response_data["exercises"][0]["nf_calories"]


# call google sheets
sheet_bearer_token = config_data["sheet"]["bearer_token"]
sheet_apikey = config_data["sheet"]["apikey"]

auth_header = {
    "Authorization": sheet_bearer_token
}

today = datetime.now().strftime("%d/%m/%Y")
print(today)
time_now = datetime.now().strftime("%H:%M:%S")
print(time_now)

data = {"workout": {
    "date": today,
    "time": time_now,
    "exercise": workout_name,
    "duration": workout_duration,
    "calories": workout_calories
}}

sheet_response = requests.post(url=f"https://api.sheety.co/{sheet_apikey}/myWorkouts2024/workouts"
                               , headers=auth_header,json=data)
print(sheet_response.text)

