from simpleutils.simpledialogs import messagebox, simpledialog
"""We maken een klasse krijger aan"""

class Krijger:
    def __init__(self,naam,levenskracht):
        self.naam = naam
        self._levenskracht = 100
    ''' hier maken we de constructor van de klasse'''

    '''hier maken we nu de methoden eten, vechten,lopen en ook roep1 en roep2'''
    def eten(self):
        self._levenskracht +=5

    def lopen(self):
        self._levenskracht -=10
    
    def vechten(self):
        self._levenskracht -=20

    def roep1(self):
        message1="Ik heb reuzenhonger"
        messagebox.showinfo("De missie"," Ik ben " + self.naam + " en ik roep: " + message1)

    def roep2(self):
        message2="Wie is de snodaard"
        messagebox.showinfo("De missie"," Ik ben " + self.naam + " en ik roep: " + message2)


    
    '''property decoraters voor de naam'''
    @property
    def levenskracht(self):
        return self._levenskracht

    @levenskracht.setter
    def levenskracht(self,value):
        if (value>100):
            raise ValueError( messagebox.showinfo("Missie", "Je kan de levenskracht niet instellen"))
        else:
            return self._levenskracht




"""uitvoerbare klasse missie"""
def  missie():
    naam = simpledialog.askstring("De missie", "Wat is de naam van de krijger?")
    krijger = Krijger(naam, 100)
    krijger.lopen()
    krijger.roep1()
    krijger.eten()
    krijger.eten()
    krijger.roep2()
    krijger.vechten()
    krijger.levenskracht = 1000
    # messagebox.showinfo("De missie", "Je kan de levenskracht niet instellen" )
    messagebox.showinfo("De Missie", "De levenskracht van " + krijger.naam + " is: " + str(krijger._levenskracht) )
   
    
missie()