from twilio.rest import Client
import requests
import os
api_key=os.getenv("AUTH_TOKEN") #"b20450dd3f31582767edb9d4c49a9d2d"

api_url=f"https://api.openweathermap.org/data/2.5/weather?q=Silver Spring&appid={api_key}"
api_5day_url="https://api.openweathermap.org/data/2.5/forecast"
api_param={
 "lat":39.95233,
 "lon":-75.16379,
 "cnt":4,
 "appid":api_key
}

response = requests.get(api_5day_url, params=api_param)
response.raise_for_status()
weather_data =  response.json()["list"]

need_umbrella = False
for weather in weather_data:
 if weather["weather"][0]["id"] < 700:
   need_umbrella=True
   break

need_umbrella=True
if need_umbrella:
 # Find your Account SID and Auth Token at twilio.com/console
 # and set the environment variables. See http://twil.io/secure
 # account_sid = "AC4e1d67335623c869f6b7c63a2882d8fe"  #

 # account_sid = os.environ["ACCOUNT_SID"]  #Working
 account_sid = os.getenv("ACCOUNT_SID")

 auth_token = "5f9b18c8c27e8c69f305c2f7f78cfcb8"  # os.environ["TWILIO_AUTH_TOKEN"]

 client = Client(account_sid, auth_token)

 message = client.messages.create(
     body="Bring an umbrella.",
     from_="+18777130724",
     to="+1 240 782 6785",
 )

 print(message.status)
else:
 print("No need for an umbrella.")



