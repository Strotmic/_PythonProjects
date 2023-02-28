"""Dit is de docstring voor de module"""


class Kaart:
    """Dit is de docString voor de klasse Kaart"""

    # Define the suits
    RUITEN = 1
    KLAVEREN = 2
    HARTEN = 3
    SHOPPEN = 4

    KLEUREN = {
        KLAVEREN: "klaveren",
        HARTEN: "Harten",
        RUITEN: "Ruiten",
        SHOPPEN: "Schoppen",
    }

    # Hieronder een dictionary in Python
    # (een niet geordende verzameling van elementen (key - value))
    SPECIALE_KAARTWAARDEN = {1: "Aas", 11: "Boer", 12: "Dame", 13: "Koning"}

    def __init__(self, kleur, waarde):
        # Save the kleur and card waarde
        self.kleur = kleur
        self.waarde = waarde

    def __lt__(self, andere_kaart):
        # Compare the card with another card
        # (return true if we are smaller, false if
        # we are larger, 0 if we are the same)
        if self.kleur < andere_kaart.kleur:
            return True
        elif self.kleur > andere_kaart.kleur:
            return False

        if self.waarde < andere_kaart.waarde:
            return True
        elif self.waarde > andere_kaart.waarde:
            return False

        return 0

    def __str__(self):
        # Return a string description of ourself
        if self.waarde in self.SPECIALE_KAARTWAARDEN:
            buf = self.SPECIALE_KAARTWAARDEN[self.waarde]
        else:
            buf = str(self.waarde)
        buf = buf + " of " + self.KLEUREN[self.kleur]

        return buf


if __name__ == "__main__":

    def uitvoeren():
        """Met deze functie voeren we alles uit"""
        kaart1 = Kaart(Kaart.SHOPPEN, 2)
        print(kaart1)

        kaart2 = Kaart(Kaart.KLAVEREN, 12)
        print(kaart2)

        print("Is schoppen 2 < klaveren 12 (klaveren dame) ?", kaart1 < kaart2)

    uitvoeren()
