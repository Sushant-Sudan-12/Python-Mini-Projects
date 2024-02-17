import requests
from datetime import datetime

TOKEN = ""
USERNAME = "sushantsudan12"
GRAPHID = "graph1"

pixal_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url = pixal_endpoint,json = user_params)
# print(response.text)


# graph1_endpoint = f"{pixal_endpoint}/{USERNAME}/graphs"
#
# graph_conifg  = {
#     "id" : GRAPHID,
#     "name" : "Code",
#     "unit" : "min",
#     "type" : "float",
#     "color" : "sora",
#
# }

headers = {
    "X-USER-TOKEN" : TOKEN,
}

# response = requests.post(url =graph1_endpoint,json=graph_conifg,headers = headers)
# print(response.text)

graph1_pixel_endpoint = f"{pixal_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = datetime.now()

pixel_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity": input("How much did you code today:"),
}

response = requests.post(url = graph1_pixel_endpoint,json = pixel_config,headers = headers)
print(response.text)








