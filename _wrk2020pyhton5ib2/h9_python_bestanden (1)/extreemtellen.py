'''Dit is de docstring voor de module'''
from mijnPackageh4.teller import Teller

class ExtreemTellen:
    '''Dit is de docString voor de klasse Teller'''

    def zetopmaximum(self, objteller):
        '''zet de teller aan en zet hem op 1000000'''
        objteller.tellerstaataan = True
        objteller.waarde = 1000000

if __name__ == '__main__':
    def uitvoeren():
        '''Met deze functie voeren we alles uit'''
        objteller = Teller()
        print(objteller.tellerstaataan)
        print("net gemaakt", objteller.waarde)

        objextremeteller = ExtreemTellen()
        objextremeteller.zetopmaximum(objteller)

        print("de toestand van de teller is nu", objteller.tellerstaataan)
        print("de waarde van de teller is nu", objteller.waarde)

    uitvoeren()
