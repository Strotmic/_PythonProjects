"""de identity operator bij lists"""
x = [1, 2, 3]
y = [1, 2, 3]

print("het id van variabele x is: ", id(x))
print("het id van variabele y is: ", id(y))


x = [1, 2, 3]
y = x

print("het id van variabele x is: ", id(x))
print("het id van variabele y is: ", id(y))
