'''Dit is de docstring voor de module'''
from mijnPackageh4.teller import Teller


class TellerGebruik3():
    '''Dit is de docString voor de klasse TellerGebruik'''

    def __init__(self):
        '''De initialisatiemethode van een class'''
        self.getal = 0

    def gebruikteller(self):
        '''Vermeerderen van de teller met 1 heeft geen effect als de teller uitstaat'''
        objteller = Teller()
        objteller.tellerstaataan = True
        objteller.increment()
        self.getal = objteller.waarde
        print("de waarde van getal is {0}".format(self.getal))

def uitvoeren():
    '''functie om de toepassing uit te voeren'''
    objtellergebruik = TellerGebruik3()
    objtellergebruik.gebruikteller()

uitvoeren()
        