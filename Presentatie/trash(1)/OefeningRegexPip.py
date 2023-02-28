from prettytable import PrettyTable
import re

myTable = PrettyTable(["Naam", "Klas", "Punten"])

myTable.add_row(["Tim", "6018", "85"])
myTable.add_row(["Andres", "6018", "80"])
myTable.add_row(["Thybe", "619", "90"])
myTable.add_row(["Johan", "619", "95"])
print(myTable)

myTable = re.sub("6018", "618 ", str(myTable))
print(myTable)

print(re.search("Tim", str(myTable)))

print(len(re.findall("618", str(myTable))))
#print(len(re.findall(["a-z"], str(myTable))))


'''We beginnen met pip install prettytable te doen, vanaf daaruit kunnen we de rest doen.

Als oefening zullen we een kleine tabel maken met 4 leerlingen. 2 uit bv 618 en 2 uit 619.

Bij een van de twee klassen maken we een typfout en dan zullen we deze typfout verbeteren aan de hand van regex. We printen zowel de grafiek voor als na de typfout af

Nadat we deze typfout hebben verbetert zullen we kijken of er een leerling met een specifieke naam in de klas zit, dit doen we ook met regex.

Als laatste zullen we dan kijken hoeveel leerlingen er van 618 inzitten.

Als alles juist loopt zou je 2 tabbelen moeten bekomen, een met de foute klas en een met de correcte klas. Dan daaronder zou je een match moeten uitkomen en dan vervolgens het nummer 2.

Dit lijkt zeer overbodig, maar als je bijvoorbeeld zo een lijst hebt met 100 leerlingen dan kan je die typfout makkelijker verbeteren of sneller zien hoeveel leerlingen er van elke klas zitten.

https://zetcode.com/python/prettytable/
https://www.geeksforgeeks.org/creating-tables-with-prettytable-library-python/
https://pypi.org/project/prettytable/
'''
