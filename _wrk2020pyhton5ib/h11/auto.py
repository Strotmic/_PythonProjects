class Auto:
    aantal_autos = 0

    def __init__(self, merk="", nummerplaat=""):
        self.merk = merk
        self.nummerplaat = nummerplaat
        Auto.aantal_autos += 1

    
x = Auto("Porsche"," AUB-123")

y = Auto("Volvo", "XYZ-456")

bericht = "Ik ben een {0} met nummerplaat {1}" 
print(bericht.format(x.merk, x.nummerplaat))
print(bericht.format(y.merk, y.nummerplaat))

print("aantal autos: " + str(Auto.aantal_autos))


  
