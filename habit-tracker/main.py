import requests

PIXE_LA_ENDPOINT="https://pixe.la/v1/users"
USERNAME="newmancroos"
TOKEN="abcedefghijk"
user_params={
    "token":"abcedefghijk",
    "username":"newmancroos",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}


# response = requests.post(url=PIXE_LA_ENDPOINT, json=user_params)
# print(response.text)

# graph_endpoint=f"{PIXE_LA_ENDPOINT}/{USERNAME}/graphs"
# graph_params={
#     "id":"graph123",
#     "name":"Reading_Graph",
#     "unit":"Pages",
#     "type":"int",
#     "color":"ajisai"
# }
# headers={
#     "X-USER-TOKEN":TOKEN
# }
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
from datetime import datetime
pixel_create_endpoint=f"{PIXE_LA_ENDPOINT}/{USERNAME}/graphs/graph123"

todays_date=datetime.now().strftime("%Y%m%d")
graph_params={
    "date":todays_date,
    "quantity":"50"
}
headers={
    "X-USER-TOKEN":TOKEN
}
response = requests.post(url=pixel_create_endpoint, json=graph_params, headers=headers)
print(response.text)

