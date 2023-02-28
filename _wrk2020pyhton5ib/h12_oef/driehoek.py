from simpleutils.simpledialogs import messagebox, simpledialog

class Driehoek:
    def __init__(self,hoogte=0,basis=0):
        self.hoogte = hoogte
        self.basis = basis

    def oppervlakte(self):
        return ((self.basis*self.hoogte)/2)


if __name__ == "__main__":
    def uitoveren():
        hoogte = simpledialog.askfloat("Venster", "Geef een hoogte op van de driehoek")
        basis = simpledialog.askfloat("Venster", "Geef een basis op van de driehoek")

        x = Driehoek(hoogte,basis)

        messagebox.showinfo("Venster", "De oppervlakte van de driehoek is: " + str(x.oppervlakte()))

    uitoveren()