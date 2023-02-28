'''Dit is de docstring voor de module'''


class Auto():
    '''Dit is de docString voor de klasse Auto'''
    aantal_autos = 0

    def __init__(self, merk="", nummerplaat=""):
        '''De initialisatie methode van een class heeft de naam __init__ '''
        self.merk = merk
        self.nummerplaat = nummerplaat
        Auto.aantal_autos += 1

if __name__ == '__main__':
    def uitvoeren():
        '''Met deze functie voeren we alles uit'''
                
        obj_bmw = Auto("bmw", "AUB123")
        print("aantal autos", Auto.aantal_autos)

        obj_porsche = Auto("porsche", "XYZ456")
        print("aantal autos", Auto.aantal_autos)

        bericht1 = "de eerste auto is een {0} met nummerplaat {1}"
        bericht2 = "de tweede auto is een {0} met nummerplaat {1}"

        print(bericht1.format(obj_bmw.merk, obj_bmw.nummerplaat))
        print(bericht2.format(obj_porsche.merk, obj_porsche.nummerplaat))

    uitvoeren()
