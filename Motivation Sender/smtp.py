import smtplib

my_email = ""
password = ""

with smtplib("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(email = my_email,password = password)
    connection.sendmail(from_addr=my_email,to_addrs="",msg = "Hello")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

print(day)
print(month)
print(year)

w_day = dt.datetime(year = 2017,month = 1,day = 14)
print(w_day)