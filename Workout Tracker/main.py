import requests

APP_ID = ""
APP_KEY = ""
URL = "https://trackapi.nutritionix.com/v2/natural/nutrients"

headers = {
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,
}
params = {
    "query":input("What did you do during your workout: "),
}

response = requests.post(url=URL,json=params,headers=headers)
result = response.json
print(result)






