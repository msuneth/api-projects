import json
import requests
from flight_data import FlightData


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

    def get_lowest_rate_for_destination(self,origin_city: str,flight_data: FlightData):
        #list_of_rates = self.get_all_rates_for_destination(origin_city,flight_data)
        return "2500"

    def get_all_rates_for_destination(self,origin_city: str,flight_data: FlightData):
        url = "https://api.tequila.kiwi.com/locations/query"
        parameters = {
           # "term": city,
            "location_types": "city"
        }
        headers = {
            "accept": "application/json",
            "apikey": self.flight_search_api_key
        }
        response = requests.get(url=url, headers=headers, params=parameters)
        return response.json()["locations"][0]["code"]
