x = 5
som = 0

print(f"het getal is: {x}")
while x <= 5:
    som += x
    x -= 1
    if x == 0:
        break

print(f"de som is: {som}")
