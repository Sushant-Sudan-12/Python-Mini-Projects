# COMMON CODES IN URL REQUESTS
# 1XX - Hold on
# 2XX - Here you go
# 3XX - Go away
# 4XX - You screwed up
# 5XX - I(website) screwed up

MY_LAT = 28.704060
MY_LNG = 77.102493
import requests
#
# response = requests.get("http://api.open-notify.org/iss-now.json")   #link to location of a satellite
# response.raise_for_status()
#
# data = response.json()
# print(data)

parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted" : 0
}
response2 = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response2.raise_for_status()

sun_data = response2.json()
print(sun_data)

