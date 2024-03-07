import requests
import json


# from datetime import datetime, timedelta
#

#
# nutritionix_apikey = config_data["nutritionix"]["API_KEY"]
# nutritionix_appid = config_data["nutritionix"]["APP_ID"]

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        with open('../config.json') as f:
            config_data = json.load(f)

        # call google sheets
        self.sheet_bearer_token = config_data["flight_deals"]["sheets_info"]["bearer_token"]
        self.sheet_apikey = config_data["flight_deals"]["sheets_info"]["api_key"]
        self.auth_header = {
            "Authorization": self.sheet_bearer_token
        }

    def read_excel(self):
        sheet_response = requests.get(url=f"https://api.sheety.co/{self.sheet_apikey}/flightDeals2024/prices"
                                       , headers=self.auth_header)
        return sheet_response

    def write_excel(self, data):
        sheet_response = requests.post(url=f"https://api.sheety.co/{self.sheet_apikey}/flightDeals2024/prices"
                                       , headers=self.auth_header, json=data)
        return sheet_response
        # data = {"price": {
        #     "date": today,
        #     "time": time_now,
        #     "exercise": workout_name,
        #     "duration": workout_duration,
        #     "calories": workout_calories
        # }}
        #
        # sheet_response = requests.post(url=f"https://api.sheety.co/{sheet_apikey}/myWorkouts2024/workouts"
        #                                , headers=auth_header, json=data)
        # print(sheet_response.text)

    def update_excel(self):
        pass

    #
    # workouts = response_data["exercises"]
    # for workout in workouts:
    #     workout_name = workout["name"].title()
    #     workout_duration = workout["duration_min"]
    #     workout_calories = workout["nf_calories"]
    #     print(response_data)
    #     today = datetime.now().strftime("%d/%m/%Y")
    #     print(today)
    #     time_now = datetime.now().strftime("%H:%M:%S")
    #     print(time_now)
    #
