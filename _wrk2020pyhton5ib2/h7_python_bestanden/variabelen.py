"""Dit is de docstring voor de module"""
from mijnPackage.teller import Teller


def variabelen():
    """Dit is de docstring voor de functie"""
    print("- een geheel getal -")
    getal1 = 5
    print(getal1)
    print(id(getal1))
    print(type(getal1))
    print("--------------------------------")
    print("- een komma getal -")
    getal2 = 1.3
    print(getal2)
    print(id(getal2))
    print(type(getal2))
    print("--------------------------------")
    print("- een tekst -")
    tekst = "hallo"
    print(tekst)
    print(id(tekst))
    print(type(tekst))
    print("--------------------------------")
    print("- een teller object -")
    obj_teller = Teller()
    print(id(obj_teller))
    print(type(obj_teller))
    print("--------------------------------")
    print("- een lijst -")
    lijst = [1, 2.2, "python"]
    print(lijst)
    print(id(lijst))
    print(type(lijst))
    print("--------------------------------")
    print("- een tuple -")
    een_tuple = (1, 2.2, "python")
    print(een_tuple)
    print(id(een_tuple))
    print(type(een_tuple))
    print("--------------------------------")
    print("- een set -")
    een_set = {5, 2, 3, 1, 4}
    print(een_set)
    print(id(een_set))
    print(type(een_set))
    print("--------------------------------")
    print("- een dictionary -")
    een_dictionary = {1: "value", "key": 2}
    print(een_dictionary)
    print(een_dictionary[1])
    print(een_dictionary["key"])
    print(id(een_dictionary))
    print(type(een_dictionary))
    print("--------------------------------")
    print("- een boolean -")
    een_boolean = True
    print(een_boolean)
    print(id(een_boolean))
    print(type(een_boolean))


variabelen()
