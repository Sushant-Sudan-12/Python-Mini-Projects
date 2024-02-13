# with open("weather_data.csv") as data:
#     data_list = data.readlines()
#

# import csv
#
# with open("weather_data.csv") as data:
#     data_list = csv.reader(data)
#     temperature = []
#     for i in data_list:
#         if i[1] == "temp":
#             pass
#         else:
#             temperature.append(int(i[1]))
#     print(temperature)

import pandas
#
# data =pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(temp_list)
# sum = 0
# n = 0
# for i in temp_list:
#     sum+=i
#     n+=1
# print(f"Average is {round(sum/n,2)}")
# print(data["temp"].mean())
# print(data[data.day=="Monday"])
# print(data[data.temp == data.temp.max()])

# data_dict = {
#     "Sekiro":[10,9,10],
#     "Elden Ring":[8,10,9],
#     "Bloodborne":[9,9,10]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("Soulslike.csv")


import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

new_data = data.Primary_Fur_Color.to_list()
print(new_data)
gray_count = 0
cinnamon_count = 0
black_count = 0
for i in new_data:
    if i =="Gray":
        gray_count+=1
    elif i == "Cinnamon":
        cinnamon_count+=1
    elif i == "Black":
        black_count+=1
new_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[gray_count,cinnamon_count,black_count]
}
f_data = pd.DataFrame(new_dict)
f_data.to_csv("Squirrel_Fur_Color_Count.csv")
