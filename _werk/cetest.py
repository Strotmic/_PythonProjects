getal = '227'

getal2 = [*getal]
getal = [*getal]
getal.reverse()

som = [int(item) for item in getal] + [int(item) for item in getal2]
print(som)

