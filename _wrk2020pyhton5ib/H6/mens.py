"""in deze module beschrijven de klasse mens"""


class Mens:
    """hieronder komt de beschrijving van de klasse mens"""

    def __init__(self, leeftijd=0, naam="Jantje"):
        self._leeftijd = leeftijd
        self.naam = naam

    def lach(self):
        message = "ik ben {0} en ik ben {1} jaar en ik lach graag hahahahahahahahahaha"
        message = message.format(self.naam, self._leeftijd)
        print(message)

    @property
    def leeftijd(self):
        """dit is de getter van java"""
        return self._leeftijd

    @leeftijd.setter
    def leeftijd(self, value):
        """dit is de setter van uit java"""
        if value < 0:
            raise ValueError("De leeftijd mag nie kleiner zijn dan 0")
        else:
            self._leeftijd = value


def mensfabriekje():
    objmens = Mens()
    objmens.lach()

    objmens.leeftijd = 18
    objmens.naam = "Den stoere Jan"
    objmens.lach()

    objmens2 = Mens(10, "Trump")
    objmens2.lach()


mensfabriekje()
