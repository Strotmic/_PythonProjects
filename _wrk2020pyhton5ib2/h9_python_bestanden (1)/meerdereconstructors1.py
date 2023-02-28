'''Dit is de docstring voor de module'''


class Teller:
    '''Dit is de docString voor de klasse Teller'''

    def __init__(self, waarde=0, tellerstaataan=False):
        '''De initialisatie methode van een class heeft de naam __init__ '''
        self._waarde = waarde
        self.tellerstaataan = tellerstaataan
        if not self.tellerstaataan:
            self._waarde = 0


    def increment(self):
        '''Vermeerderen van de teller met 1 heeft geen effect als de teller uitstaat'''
        if self.tellerstaataan:
            self._waarde += 1  # python heeft geen ++ operator

    def reset(self):
        '''Resetten van de teller heeft geen effect als de teller uitstaat'''
        if self.tellerstaataan:
            self._waarde = 0

    @property
    def waarde(self):
        '''dit is de getter van de property waarde'''
        if self.tellerstaataan:
            returnwaarde = self._waarde
        else:
            returnwaarde = 0
        return returnwaarde

    @waarde.setter
    def waarde(self, value):
        '''dit is de setter van de property waarde'''
        self._waarde = value

if __name__ == '__main__':
    def uitvoeren():
        '''Met deze functie voeren we alles uit'''
        objteller = Teller()
        print("de waarde van objteller is", objteller.waarde)
        print("toestand teller objteller is", objteller.tellerstaataan)

        objteller2 = Teller(5)
        print("de waarde van objteller2 is", objteller2.waarde)
        print("toestand teller objteller2 is", objteller2.tellerstaataan)

        objteller3 = Teller(10, True)
        print("de waarde van objteller3 is", objteller3.waarde)
        print("toestand teller objteller3 is", objteller3.tellerstaataan)

        objteller4 = Teller(20, False)
        print("de waarde van objteller4 is", objteller4.waarde)
        print("toestand teller objteller4 is", objteller4.tellerstaataan)


uitvoeren()
