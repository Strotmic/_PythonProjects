from re import M


list = [1,2,3,4,4]
lijst =[]
for i in list:
    if i not in lijst:
        lijst.append(i)
        print(i)