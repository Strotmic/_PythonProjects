from simpleutils.simpledialogs import messagebox, simpledialog


#input
temperatuur = simpledialog.askfloat("Vriezen", "geef de temperatuur op")



#output
if temperatuur <= 0:
  messagebox.showinfo("Vriezen", "het vriest en het is "+ str(temperatuur) + "° C")
else:
  messagebox.showinfo("Vriezen", "het vriest niet en het is "+ str(temperatuur) + "° C")



