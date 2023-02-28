"""docstring voor de module"""
from mijnPackageh4.teller import Teller


def uitvoeren():
    """functie om de toepassing uit te voeren"""
    objteller = Teller()

    objteller.tellerstaataan = True
    objteller.tellerstaataan = False
    toestand = objteller.tellerstaataan
    stand = objteller.waarde

    objteller.waarde = 10


uitvoeren()
