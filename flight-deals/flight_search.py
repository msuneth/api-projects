import json
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        with open('../config.json') as f:
            config_data = json.load(f)
        self.flight_search_api_token = config_data["flight-search"]["host"]

