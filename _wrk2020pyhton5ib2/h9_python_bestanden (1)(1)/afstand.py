class Afstand:
    def __init__(self):
        self._meter = 0
    
    @property
    def meter(self):
        return self._meter

    @meter.setter
    def meter(self,value):
        if value <0:
            self._meter =0
        else:
            self._meter = value

    def bereken_aantal_miles(self, aantal=0):
        self.meters = aantal /1609.344
        return self._meter 
    
    def bereken_aantal_meter(self, aantal2=0):
        self.meters = aantal2 * 1609.344
        return self._meter 

    def miles(self, value):
        self._meter = value
        
    
if __name__ == '__main__':
    def x():
        y = Afstand()
        y.meter = 1609.344

        print("1 mile is 1609.344 meter")
        print("1609.344 meter is 1.0 mile")
        print("========== kort ==========")
        print("parameter aantal miles instellen op "  + str(y.bereken_aantal_miles()) + " : " + str(y.bereken_aantal_meter()))

        y.meter = 2000
        print("parameter aantal meter instellen op "  + str(y.meter) + " : " + str(y.bereken_aantal_miles()))

        print("=============negatieve waarden=============")
        y.meter = -10
        print("parameter aantal miles instellen op -10 : " + str(y.bereken_aantal_meter()))
        print("parameter aantal meter instellen op -10 : " + str(y.bereken_aantal_miles()))
    x()




        
            
