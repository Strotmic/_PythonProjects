x = list(("Tim", "Andres", "Daniil"))

print(f"Er zijn {len(x)} leerlingen")

for i in x:
    print(f"woohoo {i} is aanwezig")

y = list(("Kobe", "Milan", "Marouane", "Lars"))

z = x+y
print(z)

z.remove("Lars")
print(z)

z.insert(4, "Rune")
print(z)

z.sort(reverse=True)
print(z)

ib619kopie = y.copy()
y.clear()
print(ib619kopie)
print(y)

print(z.count("Rune"))

test = [x.upper() for x in z]
print(test)
