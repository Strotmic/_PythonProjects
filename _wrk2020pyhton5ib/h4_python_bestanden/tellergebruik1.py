"""Dit is de docstring voor de module"""
from mijnPackageh4.teller import Teller


class TellerGebruik:
    """Dit is de docString voor de klasse TellerGebruik"""

    def __init__(self):
        """De initialisatiemethode van een class"""
        self.teller = Teller()

    def gebruikteller(self):
        """Vermeerderen van de teller met 1 heeft geen effect als de teller uitstaat"""
        self.teller.increment()
        self.teller.tellerstaataan = True
        self.teller.increment()
        self.teller.increment()
        print("de waarde van de teller is {0}".format(self.teller.waarde))


def uitvoeren():
    """functie om de toepassing uit te voeren"""
    objtellergebruik = TellerGebruik()
    objtellergebruik.gebruikteller()


uitvoeren()
