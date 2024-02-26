import requests

# API_KEY = "d8b5e5a49aa4c6eb71632c7df7e5a0a8"
# MY_LAT =
# MY_LONG =

parameters = {
    "appid": "d8b5e5a49aa4c6eb71632c7df7e5a0a8",
    "lat": 7.383017,
    "lon": 79.845523,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
data = response.json()
#print(data['list'][0]['weather'][0]['id'])
is_rain = False
for item in data['list']:
    print(item['weather'][0]['id'])
    if item['weather'][0]['id'] < 700:
        is_rain = True
if is_rain:
    print("Bring umbrella")


#https://api.openweathermap.org/data/2.5/forecast?lat=79.8352767&lon=7.3706207&appid=d8b5e5a49aa4c6eb71632c7df7e5a0a8