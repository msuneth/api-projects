# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

data_manager = DataManager()
print(data_manager.read_excel().json())

data = {"price": {
    "city": "Colombo",
    "iataCode": "Test",
    "lowestPrice": "1000"
}}

flight_info = FlightSearch()
print(flight_info.search_iata_by_city("Colombo"))
# print(data_manager.write_excel(data).json())
# print(data_manager.update_excel(data,11).json())
# notifications = NotificationManager()
# #notifications.send_sms("+94770675528","Test SMS")
# notifications.send_email("msuneth@gmail.com","Subject:Test\n\nTest")


