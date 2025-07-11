import requests
from datetime import datetime, timedelta, date
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWs_API_KEY="8d78412b49304dddb39c0ed05fdfe265"

#STOCK_API_KEY="9I7NX51LPUWNHQ7O"
#STOCK_API_KEY="6D5KCQ2WGKE6KXDV"
STOCK_API_KEY="AYNXRW6ZL9UDI88H"

parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response =requests.get(STOCK_ENDPOINT, params=parameters)
# print(response.json())
data = response.json()["Time Series (Daily)"] #["2025-07-03"]["4. close"] #[yesterday_date]
print(data)
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price=yesterday_data["4. close"]
# print(yesterday_closing_price)
day_before_yesterday_daya = yesterday_data = data_list[1]
day_before_yesterday_closing_price= day_before_yesterday_daya["4. close"]
# print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

percentage_difference = 100 * (difference / float(yesterday_closing_price))
print(percentage_difference)
# if percentage_difference > 5:
news_parameters = {
    "apiKey":NEWs_API_KEY,
    "qInTitle":COMPANY_NAME
}
news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
articles = news_response.json()["articles"]

three_articles = articles[0:3]
print(three_articles)

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

