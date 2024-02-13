import requests
import smtplib

email =""
password = ""
rain_msg ="""Subject : Will rain

Stay at home"""

no_rain= """Subject : Will not rain

Stay Happy"""

EndPoint = "https://api.openweathermap.org/data/2.5/weather"
apikey = "63f0c3be27b1e1cbac578aec8b89a0a6"

weather_param = {
    "lat": 28.704060,
    "lon": 77.102493,
    "appid":apikey,
    "cnt":4,
}

response = requests.get(EndPoint,params = weather_param)
data = response.json()
weather_code = data["weather"][0]["id"]
if(weather_code < 700):
    msg = rain_msg
else:
    msg = no_rain
print(msg)
with smtplib.SMTP("smtp-mail.outlook.com") as connection:
    connection.starttls()
    connection.login(email,password)
    connection.sendmail(from_addr=email,to_addrs=email,msg=msg)





