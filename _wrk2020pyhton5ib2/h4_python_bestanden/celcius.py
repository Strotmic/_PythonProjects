"""in deze module beschrijven we de klasse Celcius"""

class Celcius:
  """dit is een klasse om graden celcius om te zetten naar farenheid"""

  def __init__(self, temperatuur=0):
    """bij het creeren van een nieuw object wordt standaard 0 als tempereatuur gebruikt ( je geeft geen temp op)
    maar als je wel een temp opgeeft via de parameter, worst die parameterwaarde gebruikt als starttemp"""
    self._temperatuur = ValueError
  
  def to_farenheid(self):
    """met deze methode doen we een omzetting van celcius naar farenheid
    en het ersultaat van die berekening wordt teruggesturrd"""
    return (self._temperatuur*1.8) +32

  @property
  def temperatuur(self):
    """dit is de getter in python"""  
    return self._temperatuur

  @temperatuur.setter
  def temperatuur(self, value):
    """dit is de setter in python"""
    if value<-273:
      #als de temp kleiner is dan -273 treedt er een fout op
      raise ValueError("de temperatuur mag niet kleiner zijn dan -273°C zijn")
    else :
      self._temperatuur = value

def uitvoeren():
  """hiermee creeeren we ene object met de klasse celcius en gebruiken we dat object"""
  objcelcius = Celcius(-300)
 


  resultaat = objcelcius.to_farenheid()
  message = "{0} graden celcius is {1} graden farenheid"
  message = message.format(objcelcius.temperatuur, resultaat)
  print(message)

uitvoeren()
  


