class Eurobedrag:
    totaal_aantal_transacties = 0
    instansies = 0

    def __init__(self,koers):
        Eurobedrag.instansies +=1
        self.euro = 0
        self.transacties = 0
        self.koers = koers

    @property
    def euro(self):
        return self._euro
    @euro.setter
    def euro(self, value):
        if value<0:
            self._euro =0
        else:
            self._euro = value     
    
    def geteuro(self, hoeveelheid):
        Eurobedrag.totaal_aantal_transacties +=1
        self.transacties +=1
        if self.koers > 1:
            self.euro = hoeveelheid / self.koers
        else : self.euro = hoeveelheid * self.koers
        return self._euro

    def berekenlokaal(self, hoeveelheid):
        Eurobedrag.totaal_aantal_transacties +=1
        self.transacties +=1
        self.euro = hoeveelheid
        waarde = self._euro * self.koers
        return waarde

def x():
    x = Eurobedrag(40.3339)
    y = Eurobedrag(1.137)
    z = Eurobedrag(0.7053)

    lokaal = 40.3339
    print(str(lokaal) + " bef in euro is " + str(x.geteuro(lokaal)))
    euro = 1
    print(str(euro) + " euro in bef is " + str(x.berekenlokaal(euro)))

    lokaal = 10
    print(str(lokaal) + " dollar in euro is " + str(y.geteuro(lokaal)))
    euro = 1
    print(str(euro) + " euro in dollar is " + str(y.berekenlokaal(euro)))

    lokaal = 10
    print(str(lokaal) + " pond in euro is " + str(z.geteuro(lokaal)))
    euro = 1
    print(str(euro) + " euro in pond is " + str(z.berekenlokaal(euro)))

    print("het aantal wissels met bef is " + str(x.transacties))
    print("totaal aantal wissels is " + str(Eurobedrag.totaal_aantal_transacties))
    print("het aantal instanties is " +str(Eurobedrag.instansies))




x()