"""docstring voor de module"""
from mijnPackageh4.teller import Teller


def uitvoeren():
    """functie om de toepassing uit te voeren"""
    objteller = Teller()
    objteller.increment()
    objteller.tellerstaataan = True
    objteller.increment()
    objteller.increment()
    print("de waarde van de teller is {0}".format(objteller.waarde))


uitvoeren()
