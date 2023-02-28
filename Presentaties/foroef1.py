x = [[1, 2, 3], ["Diellon", "Hanne", "Daria"]]


for i in x[0]:
    print(i, ":", x[1][i-1])

print("-------------")
y = {"Diellon", "Hanne", "Daria"}
z = 1
for i in y:
    print(z, ":", i)
    z += 1
