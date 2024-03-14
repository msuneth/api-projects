class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, departure_airport_code, departure_city,currency,price=0):
        self.price = price
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city
        self.currency = currency
