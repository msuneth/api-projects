# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

# read excel data
data_manager = DataManager()
# data_source = "sheety"
data_source = "csv_file"

origin_city = "LON"
currency = "GBP"
# update data in excel
flight_info = FlightSearch()

if data_source == "sheety":
    flight_data = data_manager.read_excel().json()
    print(flight_data["prices"])
    for index, item in enumerate(flight_data["prices"]):
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
else:
    flight_required_data = data_manager.read_file()
    # print(flight_required_data)
    for index, row in flight_required_data.iterrows():
        print(index, row["City"])
        if row["IATA Code"] == "":
            iata_code = flight_info.search_iata_by_city(row["City"])
        else:
            iata_code = row["IATA Code"]
        flight_data = FlightData(iata_code, row["IATA Code"], currency)
        if iata_code != "None":
            low_rates = flight_info.get_lowest_rate_for_destination(origin_city, flight_data)
            flight_required_data.loc[index] = {'City': row["city"], 'IATA Code': iata_code, 'Lowest Price': low_rates}
            # data = {"price": {
            #     "city": row["city"],
            #     "iataCode": iata_code,
            #     "lowestPrice": low_rates,
            # }}
            data_manager.write_file(flight_required_data)

# print(flight_data)

# print(data_manager.update_excel(data, 11).json())

# print(data_manager.write_excel(data).json())
#

# notifications = NotificationManager()
# #notifications.send_sms("+94770675528","Test SMS")
# notifications.send_email("msuneth@gmail.com","Subject:Test\n\nTest")
