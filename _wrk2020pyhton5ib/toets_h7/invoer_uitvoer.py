'''Dit is de docstring voor de module'''

from simpleutils.simpledialogs import messagebox, simpledialog

# welcome the user
messagebox.showinfo("Welkom", "Dit is het welkomstbericht")

# get input
tekst = simpledialog.askstring("Titel van het venstertje", "Geef een tekst op")
geheel_getal = simpledialog.askinteger("Titel van het venstertje", "Geef een geheel getal op")
komma_getal = simpledialog.askfloat("Titel van het venstertje", "Geef een kommagetal op")
print(tekst)
print(geheel_getal)
print(komma_getal)

# output
outputtekst = "Hallo het is mooi weer vandaag"
outputgetal = 5

# show output
messagebox.showinfo("Titel van het venstertje", outputtekst)
messagebox.showinfo("Titel van het venstertje", outputgetal)
