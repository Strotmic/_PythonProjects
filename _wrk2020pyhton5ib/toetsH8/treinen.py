from simpleutils.simpledialogs import messagebox, simpledialog

def trein():
    #input
    snelheidA = simpledialog.askfloat("Treinen", "geef een snelheid op voor de eerste trein (in km/u)")
    tijdA = simpledialog.askfloat("Treinen", "geef een tijd op voor de eerste trein (in uren)")

    snelheidB = simpledialog.askfloat("Treinen", "geef een snelheid op voor de tweede trein (in km/u)")
    tijdB = simpledialog.askfloat("Treinen", "geef een tijd op voor de tweede trein (in uren")

    totaleAfstand = simpledialog.askfloat("Treinen" , "Geef een totale afstand op in kilometers")


    #verwerking en uitvoer

    #dit berkent of de treinen zullen botsen
    if ((snelheidA * tijdA) + (snelheidB * tijdB) >= totaleAfstand):

        messagebox.showerror("Treinen", "De treinen zullen botsen")

    else:
        messagebox.showinfo("Treinen", "De treinen zullen niet botsen")


trein()