'''Dit is de docstring voor de module'''


class Teller():
    '''Dit is de docString voor de klasse Teller'''

    def __init__(self):
        '''De initialisatie methode van een class heeft de naam __init__ '''
        self._waarde = 0
        self.tellerstaataan = False

    def increment(self):
        '''Vermeerderen van de teller met 1 heeft geen effect als de teller uitstaat'''
        if self.tellerstaataan:
            self._waarde += 1  # python heeft geen ++ operator

    def decrement(self):
        '''Verminderen van de teller met 1 heeft geen effect als de teller uitstaat'''
        if self.tellerstaataan:
            self._waarde -= 1  # python heeft geen ++ operator
     
    def verdubbel(self):
        '''verdubbelen van de teller met 2 heeft geen effect als de teller uitstaat'''
        if self.tellerstaataan:
            self._waarde *= 2  # python heeft geen ++ operator

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
        print("net gemaakt", objteller.waarde)

        objteller.increment()
        print("increment zonder aan te zetten", objteller.waarde)

        objteller.tellerstaataan = True
        print("teller aanzetten en waarde printen", objteller.waarde)

        objteller.increment()
        print("waarde teller na increment", objteller.waarde)

        objteller.decrement()
        print("waarde teller na decrement", objteller.waarde)

        objteller.decrement()
        print("waarde teller na decrement", objteller.waarde)

        objteller.verdubbel()
        print("waarde teller na verdubbelen",objteller.waarde)


    uitvoeren()
