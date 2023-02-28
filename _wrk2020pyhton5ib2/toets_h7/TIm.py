    
from simpleutils.simpledialogs import messagebox, simpledialog
"""We maken een klasse krijger"""
class Krijger:
    """We maken een constructor"""
    def __init__(self, naam, levenskracht):
        self._naam = naam
        self._levenskracht = 100
    """We maken een getter en een setter voor naam"""
    @property
    def naam(self):
        return self._naam

    @naam.setter
    def naam(self):
        return self._naam
    """We maken methodes"""
    def eten(self):
        self._levenskracht += 5
    
    def lopen(self):
        self._levenskracht -= 10

    def vechten(self):
        self._levenskracht -= 20

    def roepen1(self):
        tekst1="ik heb reuze honger"
        messagebox.showinfo("De missie","Ik ben " + self.naam + " en ik roep: " + tekst1)

    def roepen2(self):
        tekst2="wie is de snoodaard?"
        messagebox.showinfo("De missie","Ik ben " + self.naam + " en ik roep: " + tekst2)

"""hier mee wordt alles uitgevoerd"""
def missie():
    naam = simpledialog.askstring("De missie", "Wat is de naam van de krijger?")
    objstrijder = Krijger(naam,100)
    objstrijder.lopen()
    objstrijder.roepen1()
    objstrijder.eten()
    objstrijder.eten()
    objstrijder.roepen2()
    objstrijder.vechten()
    tekst3="Je kan de levenskracht niet instellen"
    messagebox.showinfo("De missie", tekst3)
    tekst4= "De levenskracht van " + objstrijder.naam + "is : " + str(objstrijder._levenskracht)
    messagebox.showinfo("De missie", tekst4)

missie()


