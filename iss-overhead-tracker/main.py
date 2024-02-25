import time
import json
import requests
from datetime import datetime
import smtplib

MY_LAT = 7.3654796
MY_LONG = 79.8328992

with open('../config.json') as f:
    config_data = json.load(f)

# Access database configuration
smtp_server = config_data['email']['host']
smtp_port = config_data['email']['port']
SENDER = config_data['email']['sender']
RECEIVER = config_data['email']['receiver']
PASSWORD = config_data['email']['password']


def send_email(sender, receiver, message):
    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=sender, password=PASSWORD)
        connection.sendmail(
            from_addr=sender,
            to_addrs=receiver,
            msg=message)


# ISS position
def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    iss_position = (latitude, longitude)
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
    return sunrise_hour,sunset_hour


while True:
    time.sleep(10)
    iss_location = get_iss_position()
    lat_diff = MY_LAT - float(iss_location[0])
    lng_diff = MY_LAT - float(iss_location[1])
    print(lat_diff, lng_diff)

    if (5 > lat_diff > -5) and (5 > lng_diff > -5):
        sun_hours = get_sunset_sunrise_hour()
        current_hour = datetime.now().hour
        print(current_hour)
        if current_hour >= sun_hours[1]:
            print("look up")
            email_msg = (f"Subject: ISS is above you!\n\n"
                         f"Look up")
            send_email(SENDER,RECEIVER,email_msg)





