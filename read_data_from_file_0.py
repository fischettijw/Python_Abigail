# https://generatedata.com/generator
# https://www.youtube.com/watch?v=gSbEXZvgyBw
# https://www.youtube.com/watch?v=0C2405R-uGk&t=193s

import os

os.system("cls")


file = open("RandomData-10.csv", "r")
data = file.readlines()
file.close()
print(data)


# with open("RandomData-10.csv", "r") as file:
#     data = file.readlines()
# print(data)


# https://www.w3schools.com/python/python_file_write.asp

file = open("Abigail_Output.txt", "w")
for person in data:
    file.write(person)
file.close()
