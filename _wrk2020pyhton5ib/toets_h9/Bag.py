from simpleutils.simpledialogs import messagebox, simpledialog

class Bag:
    bag =0
    glazen =0
    tijd =0
    def __init__(self, naam="", gewicht=0, geslacht=0 ):
        self.naam = simpledialog.askstring("Feestje", "Wat is uw naam?")
        self.gewicht = simpledialog.askinteger("Feestje", "Wat is uw gewicht?")
        self.geslacht = simpledialog.askinteger("Feestje", "Wat is uw geslacht? 1=man / 2=vrouw")
    def bereken_bag(self, glazen=0, tijd=0):
        Bag.glazen = simpledialog.askinteger("Feestje", "Hoeveel glazen heb je gedronken?")
        Bag.tijd = simpledialog.askfloat("Feestje","Hoeveel uren ondertussen na je eerste glas?")
        if self.geslacht==1:
           Bag.bag =  ((Bag.glazen *10)/(self.gewicht * 0.72))-((Bag.tijd-0.5)*(self.gewicht *0.002))
        
        if self.geslacht==2:
            Bag.bag =  ((Bag.glazen *10)/(self.gewicht * 0.61))-((Bag.tijd-0.5)*(self.gewicht *0.002))
        return Bag.bag
    def dronken(self):
        if Bag.bag<0.5:
           messagebox.showinfo("Feestje", self.naam + " je dronk " + str(Bag.glazen) + " glazen en na " + str(Bag.tijd) + " uur ben je niet (meer) dronken" )
        else:
           messagebox.showinfo("Feestje", self.naam + " je dronk " + str(Bag.glazen) + " glazen en na " + str(Bag.tijd) + " uur ben je nog steeds dronken en je BAG is: " + str(Bag.bag)  )


if __name__ == "__main__":

    def x():
        objmens = Bag()
        objmens.bereken_bag()
        objmens.dronken()

    x()