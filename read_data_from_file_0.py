# https://generatedata.com/generator

import os

os.system("cls")


file = open("RandomData-10.csv", "r")
data = file.readlines()
file.close()
print(data)


# with open("RandomData-10.csv", "r") as file:
#     data = file.readlines()
# print(data)
