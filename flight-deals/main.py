# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

from data_manager import DataManager

data_manager = DataManager()
print(data_manager.read_excel().json())

data = {"price": {
    "city": "Colombo",
    "iataCode": "Test",
    "lowestPrice": "1000"
}}
print(data_manager.write_excel(data).json())
print(data_manager.update_excel(data,11).json())

