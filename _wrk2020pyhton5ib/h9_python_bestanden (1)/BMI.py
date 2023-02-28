class Bmi:
    def __init__(self, lengte=0, massa=0):
        self.lengte= lengte
        self.massa= massa

    def bmi(self):
        if self._lengte<=0:
            value = 0
        else:
            value = (self._massa/(self._lengte*self._lengte))
        return value


    @property 
    def lengte(self):
        return self._lengte
    @lengte.setter
    def lengte(self,value):
        if value<0:
            self._lengte = 0
        else:
            self._lengte = value
     

    @property 
    def massa(self):
        return self._massa
    @massa.setter
    def massa(self,value):
        if value<0:
            self._massa = 0
        else:
            self._massa= value
    



if __name__ == '__main__':
    def x():
        objbmi1 = Bmi()
        print("net gemaakt objbmi zonder parameters")
        print("met als massa",objbmi1.massa)
        print("met als lengte",objbmi1.lengte)
        print("met als bmi",objbmi1.bmi())

        objbmi2 = Bmi(1.8,81)
        print("net gemaakt objbmi2 met een parameter voor de lengte en de massa")
        print("met als massa",objbmi2.massa)
        print("met als lengte",objbmi2.lengte)
        print("met als bmi",objbmi2.bmi())

        objbmi3 = Bmi(-1.5,-85)
        print("net gemaakt objbmi3 met negatieve parameters voor de lengte en de massa")
        print("met als massa",objbmi3.massa)
        print("met als lengte",objbmi3.lengte)
        print("met als bmi",objbmi3.bmi())

        objbmi4 = Bmi(1.8,)
        print("net gemaakt objbmi4 met alleen een parameter voor de lengte")
        print("met als massa",objbmi4.massa)
        print("met als lengte",objbmi4.lengte)
        print("met als bmi",objbmi4.bmi())

        objbmi5 = Bmi(0,80)
        print("net gemaakt objbmi5 met alleen een parameter voor de massa")
        print("met als massa",objbmi5.massa)
        print("met als lengte",objbmi5.lengte)
        print("met als bmi",objbmi5.bmi())
        
        
x()