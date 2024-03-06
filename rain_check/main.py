import requests
import os
from twilio.rest import Client
import json

with open('../config.json') as f:
    config_data = json.load(f)

account_sid = config_data["twilio"]["account_sid"]
auth_token = config_data["twilio"]["auth_token"]

# account_sid = os.environ.get("account_sid")
# print(account_sid)
# auth_token = os.environ.get("auth_token")
# appid = os.environ.get("appid")

# parameters = {
#     "appid": appid,
#     "lat": 7.383017,
#     "lon": 79.845523,
#     "cnt": 4,
# }
#
# response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
# response.raise_for_status()
# data = response.json()
# #print(data['list'][0]['weather'][0]['id'])
# is_rain = False
# for item in data['list']:
#     print(item['weather'][0]['id'])
#     if item['weather'][0]['id'] < 900:
#         is_rain = True

is_rain = True
if is_rain:
    print("Bring umbrella")
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Bring umbrella",
        from_='+19309662195',
        to='+94770675528'
    )

    print(message.sid)


#https://api.openweathermap.org/data/2.5/forecast?lat=79.8352767&lon=7.3706207&appid=d8b5e5a49aa4c6eb71632c7df7e5a0a8