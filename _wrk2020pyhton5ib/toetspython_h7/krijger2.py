from simpleutils.simpledialogs import messagebox, simpledialog
"""We maken een klasse krijger aan"""

class Krijger:
    def __init__(self, naam):
        self.naam = naam
        self._levenskracht = 100

    def eten(self):
        self._levenskracht +=5
    
    def lopen(self):
        self._levenskracht -=10

    def vechten(self):
        self._levenskracht -=20

    def roepen(self, kreet):
        bericht = "Ik ben " + self.naam + " en ik roep " + kreet
        messagebox.showinfo("De krijger", bericht)

    @property
    def levenskracht(self):
        return self._levenskracht

    @levenskracht.setter
    def levenskracht(self,value):
        messagebox.showwarning("De Krijger", "je mag de levenskracht niet instellen")


def missie():
    naam = simpledialog.askstring("De missie","wat is de naam van de krijger")
    x = Krijger(naam)  
    
    x.lopen()
    x.roepen("Ik heb reuzenhonger")
    x.eten()
    x.eten()
    x.roepen("Wie is de snodaard")
    x.vechten()

    bericht = "ik ben" + x.naam + "en mijn levenskracht is " + str(x.levenskracht)
    messagebox.showinfo("De missie", bericht)

    x.levenskracht = 1000

    messagebox.showinfo("De missie", bericht)


missie()

    
