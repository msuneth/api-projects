# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

# read excel data
data_manager = DataManager()
try:
    excel_data = data_manager.read_excel().json()
    print(excel_data)
except KeyError:
    file_data = data_manager.read_file()
    print(file_data)
origin_city = "LON"
currency = "GBP"
# update data in excel
flight_info = FlightSearch()
for index, item in enumerate(excel_data["prices"]):
    print(index, item["city"])
    if item["iataCode"] == "":
        iata_code = flight_info.search_iata_by_city(item["city"])
    else:
        iata_code = item["iataCode"]
    flight_data = FlightData(iata_code, item["city"], currency)
    if iata_code != "None":
        low_rates = flight_info.get_lowest_rate_for_destination(origin_city, flight_data)
        data = {"price": {
            "city": item["city"],
            "iataCode": iata_code,
            "lowestPrice": low_rates,
        }}
        data_manager.update_excel(data, index + 2)

print(excel_data)

# print(data_manager.update_excel(data, 11).json())

# print(data_manager.write_excel(data).json())
#

# notifications = NotificationManager()
# #notifications.send_sms("+94770675528","Test SMS")
# notifications.send_email("msuneth@gmail.com","Subject:Test\n\nTest")
