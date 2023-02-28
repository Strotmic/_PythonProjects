#declareer een variabele en geef ze een beginwaarde
f = 101
print(f)

#globale vs lokale variabelen in functies
def someFunction():
    global f
    f = "I'm learning Python"
    print(f)

someFunction()
print(f)
