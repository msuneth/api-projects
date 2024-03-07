import requests
import json


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

    def update_excel(self, data, change_id):
        sheet_response = requests.put(url=f"https://api.sheety.co/{self.sheet_apikey}/flightDeals2024/prices/{change_id}"
                                       , headers=self.auth_header, json=data)
        return sheet_response

    def write_excel(self,data):
        sheet_response = requests.post(url=f"https://api.sheety.co/{self.sheet_apikey}/flightDeals2024/prices"
                                       , headers=self.auth_header, json=data)
        return sheet_response

