class Auto:
  def __init__(self, snelheid=0):
    self._snelheid = 0
    self.autostaataan = False

  def versnellen(self):
    if self.autostaataan:
      self._snelheid += 10
  def vertragen(self):
    if self.autostaataan:
      self.snelheid -= 10
  def stoppen(self):
    if self.autostaataan:
      self._snelheid = 0

  @property
  def snelheid(self):
    if self.autostaataan:
      returnsnelheid = self._snelheid
    else:
      returnsnelheid = 0
    return returnsnelheid

  @snelheid.setter
  def snelheid(self, value):
    if value<0:
      raise ValueError("de snelheid moet boven 0 zijn")
    else:
      self.snelheid = value

if __name__ == "__main__": 
  
  def uitvoeren():


    auto = Auto(0)

    auto.autostaataan = True
    auto.versnellen()
    message = "de auto rijd {0} km per uur"
    message = message.format(auto.snelheid)
    print(message)
  
  uitvoeren()

  
