import time

import requests

MY_LAT = 7.3654796
MY_LONG = 79.8328992


# ISS position
def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    iss_position = (latitude, longitude)
    print(iss_position)
    return iss_position


# Sunset-sunrise time
def get_sunset_sunrise_hour():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Asia/Colombo"
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset_hour = data["results"]["sunset"].split("T")[1].split(":")[0]
    print(sunrise_hour,sunset_hour)
    return sunrise_hour,sunset_hour


while True:
    time.sleep()

