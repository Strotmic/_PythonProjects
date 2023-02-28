from simpleutils.simpledialogs import messagebox, simpledialog



  
getal = simpledialog.askstring("BesturingE", "Geef een getal op")

lengte = len(getal)

i = lengte -1
while i<=lengte:  
    messagebox.showinfo("BesturingE ", "Het getal is " + str(getal[i]))
    i -=1
    if i < 0:
        break

