from simpleutils.simpledialogs import messagebox, simpledialog


def uitvoeren():

  #welkomscherm
  messagebox.showinfo("Welkom", "Hier zullen we de oppervlakte van een driehoek berekenen")

  #basis input en output
  basis = simpledialog.askinteger("Basis", "Geef een basis op")
  messagebox.showinfo("de basis is", basis)

  #hoogte input en output
  hoogte = simpledialog.askinteger("Hoogte", "geef een hoogte op")
  messagebox.showinfo("de hoogte is", hoogte)

  # variabele van oppervlakte maken en berekenen
  oppervlakte = (basis * hoogte) / 2 

  #oppervlakte tonen
  messagebox.showinfo("de oppervlakte is", oppervlakte)

uitvoeren()