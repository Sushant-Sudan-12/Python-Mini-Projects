#LIST COMPREHENSION

list = [1,2,3]
new_list = [n*2 for n in list]
print(list)
print(new_list)

list = [n*2 for n in range(1,5)]
print(list)

list = ["Andy","Bharat","Chepuri","Dayne"]
new_list =[n for n in list if len(n)<6]
print(list)
print(new_list)

#DICTIONARY COMPREHENSION

import random

name = ["Andy","Bharat","Chepuri","Dayne"]
dict = {student:random.randint(80,100) for student in name}
print(dict)
passed = {student:score for (student,score) in dict.items() if score > 90}
print(passed)

#PANDAS DATAFRAME

import pandas as pd

student_dict = {
    "student":["Akash","Patil","Vivek"],
    "score":[69,75,98]
}
new_dataframe = pd.DataFrame(student_dict)
print(new_dataframe)
for (index,row) in new_dataframe.iterrows():
    print(row)





