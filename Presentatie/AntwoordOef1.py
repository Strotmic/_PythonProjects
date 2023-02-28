import re
from string import Template

name=input("Geef de naam op ")
surname=input("Wat is de achternaam ")

print(f"De naam is {name} en de achternaam is {surname}")
print("De naam is {0} en de achternaam is {1}".format(name,surname))
print("De naam is %s en de achternaam is %s" % (name,surname))

x = Template("De naam is $x en de achternaam is $y")
print(x.substitute(x=name,y=surname))

x = "De naam is x en de achternaam is y"
x = re.sub("x",name,x)
x = re.sub("y",surname,x)
print(x)
