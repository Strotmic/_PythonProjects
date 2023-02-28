uur = 2
afstand = 75

x = afstand/uur


print(f"de snelheid is {x}")
if x < 15:
    print("Je fietsts traag")
elif x >= 15 and x < 18:
    print("je fietste gemmideld")
elif x >= 18 and x < 23:
    print("Je fietst aan een degelijk tempo")
else:
    print("je fietst heel snel, heb je een elektrische fiets?")
