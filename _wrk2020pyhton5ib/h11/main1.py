"""als we onderstaande code uitvoeren vanuit main1.py dan
wordt deze code uitgevoerd van uit het hoofdprogramma"""

if __name__ == "__main__":
    print("This program is being run by itself")
    print("de waarde van __name__ is", __name__)
else:
    print("I am being imported from another module")
    print("de waarde van __name__ is", __name__)
