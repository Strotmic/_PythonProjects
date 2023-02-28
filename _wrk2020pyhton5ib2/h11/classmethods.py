"""Dit is de docstring voor de module"""
import random


class Cheese:
    """dit is een docstring"""

    def __init__(self, num_holes=0):
        """defaults to a solid cheese"""
        self.number_of_holes = num_holes

    @classmethod
    def willekeurig(cls):
        """dit is een docstring"""
        return cls(random.randint(0, 100))

    @classmethod
    def slightly_holey(cls):
        """dit is een docstring"""
        return cls(random.randint(0, 33))

    @classmethod
    def very_holey(cls):
        """dit is een docstring"""
        return cls(random.randint(66, 100))


if __name__ == "__main__":

    def uitvoeren():
        """Met deze functie voeren we alles uit"""
        gouda = Cheese()
        print("Aantal gaten Gouda: " + str(gouda.number_of_holes))

        vijfgaten = Cheese(5)
        print("Aantal gaten in vijfgaten: " + str(vijfgaten.number_of_holes))

        emmentaler = Cheese.willekeurig()
        print("Aantal gaten Emmental: " + str(emmentaler.number_of_holes))

        leerdammer = Cheese.slightly_holey()
        print("Aantal gaten Leerdammer: " + str(leerdammer.number_of_holes))


uitvoeren()
