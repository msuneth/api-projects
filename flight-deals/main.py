# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

# read excel data
data_manager = DataManager()
excel_data = data_manager.read_excel().json()
print(excel_data)

# update data in excel
flight_info = FlightSearch()
for index, item in enumerate(excel_data["prices"]):
    print(index,item["city"])
    iata_code = flight_info.search_iata_by_city(item["city"])
    item['iataCode'] = iata_code
    data = {"price": {
        "city": item["city"],
        "iataCode": iata_code,
        "lowestPrice": "1000"
    }}
    data_manager.update_excel(data, index+2)

print(excel_data)


# print(data_manager.update_excel(data, 11).json())

# print(data_manager.write_excel(data).json())
#

# notifications = NotificationManager()
# #notifications.send_sms("+94770675528","Test SMS")
# notifications.send_email("msuneth@gmail.com","Subject:Test\n\nTest")


