import random

list_1 = ["Hello", "2", "world", ":-)"]
list_2=[]
# print("Введите массив: ")
# list_1=input().split(',')

for i in range(random.randint(0,3)):
    rand=random.choice(list_1)
    if rand not in list_2:
        list_2.append(rand)
print (list_2)
