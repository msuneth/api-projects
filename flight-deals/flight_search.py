import json
import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        with open('../config.json') as f:
            config_data = json.load(f)
        self.flight_search_api_key = config_data["flight_deals"]["flight-search"]["api_key"]

    def search_iata_by_city(self, city):
        url = "https://api.tequila.kiwi.com/locations/query"
        parameters = {
            "term": city,
            "location_types": "city"
        }
        headers = {
            "accept": "application/json",
            "apikey": self.flight_search_api_key
        }
        response = requests.get(url=url, headers=headers, params=parameters)
        return response.json()["locations"][0]["code"]
