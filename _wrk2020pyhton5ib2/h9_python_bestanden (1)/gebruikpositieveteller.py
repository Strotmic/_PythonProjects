'''Dit is de docstring voor de module'''

from mijnPackageh9.positieveteller import PositieveTeller

def uitvoeren():
    '''Dit is de docstring voor de functie'''
    objteller = PositieveTeller()
    objteller.tellerstaataan = True
    objteller.increment()
    print(objteller.waarde)
    objteller.increment(-10)
    print(objteller.waarde)

uitvoeren()
