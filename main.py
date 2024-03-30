import random

list_1 = ["Hello", "2", "world", ":-)"]
list_2=[]
# print("Введите массив: ")
# list_1=input().split(',')

for i in list_1:
    if len(i) <=3:
        list_2.append(i)
print (list_2)

