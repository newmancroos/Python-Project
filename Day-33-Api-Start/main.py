import requests

# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# print(response.status_code)
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
# print((latitude, longitude))


quotsresponse = requests.get("http://api.kanye.rest")
quotsresponse.raise_for_status()
print(quotsresponse.json()["quote"])