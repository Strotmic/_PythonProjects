personen = float(input("Hoeveel mensen gaan op reis? "))
prijs = float(input("Wat is de prijs van de vlucht? "))
nachten = float(input("Hoeveel nachten wordt er geboekt? "))
pnacht = float(input("Wat is de prijs per nacht? "))
zomeractie = input("Zomeractie ")

if zomeractie == 'nee':
    print(f'De reis voor de volledige groep kost: {(personen*(prijs+(nachten*pnacht)))+20}')
else:
    print(f'De reis voor de volledige groep kost: {((personen*(prijs+(nachten*pnacht)))+20)*0.9}')