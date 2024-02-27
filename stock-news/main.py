import requests
import json
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
from datetime import date,timedelta

with open('../config.json') as f:
    config_data = json.load(f)

smtp_server = config_data['email']['host']
smtp_port = config_data['email']['port']
SENDER = config_data['email']['sender']
RECEIVER = config_data['email']['receiver']
PASSWORD = config_data['email']['password']
stock_apikey = config_data['api_keys']['stockapi']
news_api = config_data['api_keys']['newsapi']

stock_parameters = {
    "apikey": stock_apikey,
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "outputsize": "compact",
}

stock_response = requests.get(url="https://www.alphavantage.co/query",params=stock_parameters)
stock_response.raise_for_status()
data = stock_response.json()
yesterday = date.today() - timedelta(days=1)
yesterday_data = data["Time Series (Daily)"][str(yesterday)]
print(data)

# day_before_yesterday = date.today() - timedelta(days=2)
# day_before_yesterday_data = data["Time Series (Daily)"][str(day_before_yesterday)]
# print(day_before_yesterday_data)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


news_response = requests.get(url=)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

