x = ("Tim", "Andres", "Dylan", "Hanne")
print(x)
print(f"Aantal leerlingen {len(x)}")

y = ("Dejonckhere",)
print(f"De leerkrach is {y} en de tuple is effectief een {type(y)}")

z = y+x
print(z)

c = list(z)
c.remove("Dylan")
z = tuple(c)
print(z)

c = list(z)
c.append("Dylan")
c.append("Hanne")
z = tuple(c)
print(z)

print(f"Hanne zit {z.count('Hanne')} keer in de lijst")
