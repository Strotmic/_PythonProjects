from simpleutils.simpledialogs import messagebox, simpledialog


random = 555
beurten = 0

while True:
    getal = simpledialog.askinteger("Random", "Geef een getal op")
    beurten +=1
    if getal>random:
        messagebox.showinfo("random", "gok lager, beurten: " + str(beurten)) 
    if getal<random:
        messagebox.showinfo("random", "gok hoger, beurten: " + str(beurten)) 

    if getal == random:
        break

messagebox.showinfo("random", "Proficiat je hebt het geraden in " + str(beurten) + " beurten")