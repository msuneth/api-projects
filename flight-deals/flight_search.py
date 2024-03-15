import json
import requests
from flight_data import FlightData
from datetime import datetime,timedelta


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
        try:
            data = response.json()["locations"][0]["code"]
            return data
        except IndexError:
            return "None"

    def get_lowest_rate_for_destination(self, origin_city: str, flight_data: FlightData):
        list_of_flights = self.get_flights_for_destination(origin_city, flight_data)
        lowest_rate = float(list_of_flights[0]['price'])
        for item in list_of_flights:
            if float(item['price']) < lowest_rate:
                lowest_rate = item['price']
        return lowest_rate

    def get_flights_for_destination(self, origin_city: str, flight_data: FlightData):
        url = "https://api.tequila.kiwi.com/v2/search"
        # 'fly_from=LON&fly_to=PRG&date_from=01%2F04%2F2024&date_to=03%2F04%2F2024'
        # '&return_from=04%2F04%2F2024&return_to=06%2F04%2F2024&nights_in_dst_from=2'
        # '&nights_in_dst_to=3&max_fly_duration=20&ret_from_diff_city=true&ret_to_diff_city=true'
        # '&one_for_city=0&one_per_date=0&adults=2&children=2&selected_cabins=C&mix_with_cabins=M'
        # '&adult_hold_bag=1%2C0&adult_hand_bag=1%2C1&child_hold_bag=2%2C1&child_hand_bag=1%2C1'
        # '&only_working_days=false&only_weekends=false&partner_market=us&max_stopovers=2'
        # '&max_sector_stopovers=2&vehicle_type=aircraft&limit=500'
        from_date = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        to_date = (datetime.now() + timedelta(days=60)).strftime("%d/%m/%Y")
        parameters = {
            "fly_from": origin_city,
            "fly_to": flight_data.departure_airport_code,
            "date_from": from_date,
            "date_to": to_date,
            "curr": flight_data.currency
        }
        headers = {
            "accept": "application/json",
            "apikey": self.flight_search_api_key
        }
        response = requests.get(url=url, headers=headers, params=parameters)
        res = response.json()['data']
        return res
