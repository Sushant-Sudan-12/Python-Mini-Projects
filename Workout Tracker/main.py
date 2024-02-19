import requests

APP_ID = "d6911353"
APP_KEY = "07ef7fd7ee8973846342d256fd81fad9"
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






