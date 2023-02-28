from simpleutils.simpledialogs import messagebox, simpledialog


jeugdbeweging = simpledialog.askinteger("Venster","Bent u een jeugdbeweging: 1=ja/2=nee")

if jeugdbeweging == 1:
    leiders = simpledialog.askinteger("Venster","Hoeveel leiders zijn er")
    personen = simpledialog.askinteger("Venster","Hoeveel leden zijn er")
    gratis = 0

    for i in range(1,personen+1):
        if (i%10==0):
            gratis +=1

    personen = personen - gratis

    prijs = (personen * 0.75)

    messagebox.showinfo("Venster", "Het aantal gekochte tickets zijn: " + str(personen + gratis + leiders) + " en de prijs is " + str(prijs))
else:
    personen = simpledialog.askinteger("Venster","Hoeveel personen zijn er")
    gratis = 0

    for i in range(1,personen+1):
        if (i%10==0):
            gratis +=1

    personen = personen - gratis

    prijs = (personen * 1.50)

    messagebox.showinfo("Venster", "Het aantal gekochte tickets zijn: " + str(personen + gratis) + " en de prijs is " + str(prijs))

