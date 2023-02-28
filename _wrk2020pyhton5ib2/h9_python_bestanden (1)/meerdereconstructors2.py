'''Dit is de docstring voor de module'''
import random

class Cheese:
    '''dit is een docstring'''
    def __init__(self, num_holes=0):
        '''defaults to a solid cheese'''
        self.number_of_holes = num_holes

    @classmethod
    def random(cls):
        '''dit is een docstring'''
        return cls(random.randint(0, 100))

    @classmethod
    def slightly_holey(cls):
        '''dit is een docstring'''
        return cls(random.randint(0, 33))

    @classmethod
    def very_holey(cls):
        '''dit is een docstring'''
        return cls(random.randint(66, 100))

if __name__ == '__main__':
    def uitvoeren():
        '''Met deze functie voeren we alles uit'''
        gouda = Cheese()
        print(gouda.number_of_holes)
        
        emmentaler = Cheese.random()
        print(emmentaler.number_of_holes)
        
        leerdammer = Cheese.slightly_holey()
        print(leerdammer.number_of_holes)

uitvoeren()
