import smtplib

import requests
import json

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
from datetime import date, timedelta

with open('../config.json') as f:
    config_data = json.load(f)

smtp_server = config_data['email']['host']
smtp_port = config_data['email']['port']
SENDER = config_data['email']['sender']
RECEIVER = config_data['email']['receiver']
PASSWORD = config_data['email']['password']
stock_apikey = config_data['api_keys']['stockapi']
news_apikey = config_data['api_keys']['newsapi']

stock_parameters = {
    "apikey": stock_apikey,
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "outputsize": "compact",
}

day_count = 1


def get_previous_day_stock_price(response_data: json):
    global day_count
    day1 = date.today() - timedelta(days=day_count)
    day_stock_price = 0.0
    try:
        # day_stock_price: float = float(response_data["Time Series (Daily)"][str(day1)]['4. close'])
        day_stock_price: float = float(response_data["Time Series (Daily)"][str(day1)]['1. open'])
    except ValueError:
        day_count += 1
        get_previous_day_stock_price(response_data)
    finally:
        day_count += 1
        return day_stock_price
    # #yesterday_stock_price = data["Time Series (Daily)"][str(yesterday)]['1. open']
    # print(data)


def get_news():
    news_parameters = {
        "apiKey": news_apikey,
        "q": COMPANY_NAME,
        "language": "en",
        "sortBy": "publishedAt",
        "searchIn": "title"
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    news_dict = {"title": news_data['articles'][0]['title'],
                 "description": news_data['articles'][0]['description']}
    print(news_dict)
    return news_dict


def send_email(stock_diff_per: float, news_dict: dict):
    show_diff = ""
    if stock_diff_per < -5:
        show_diff = f"🔻{int(stock_diff_per)}"
    if stock_diff_per > 5:
        show_diff = f"🔺{int(stock_diff_per)}"

    stock_news_msg = f"""Subject:{STOCK} stock alert\n\n
    TSLA: {show_diff}%
    Headline: {news_dict['title']} 
    Brief: {news_dict['description']}
    """
    print(stock_news_msg)
    msg = stock_news_msg.encode('utf-8')
    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=SENDER, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER,
            to_addrs=RECEIVER,
            msg=msg)


stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()
data = stock_response.json()
print(data)
data_list = [value for key, value in data['Time Series (Daily)'].items()]
#day1_stock_price = get_previous_day_stock_price(data)
day1_stock_price = float(data_list[0]['4. close'])
#day2_stock_price = get_previous_day_stock_price(data)
day2_stock_price = float(data_list[1]['4. close'])
diff = day2_stock_price - day1_stock_price
print(diff)
stock_difference_percentage = diff * 100 / day1_stock_price
if stock_difference_percentage > 5 or stock_difference_percentage < -5:
    news_info = get_news()
    send_email(stock_difference_percentage, news_info)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
# stock_going_up_msg = """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """
# stock_going_down_msg = """TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """
