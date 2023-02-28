class Deur():
  """nieuwe klases met de naam deur"""
  def __init__(self, breedte=83, hoogte=201.5):
    """dit is de constructor die we hier maken"""
    self.breedte = breedte
    self.hoogte = hoogte
  
  def oppervlakte(self):
    """dit is een methode voor de oppervlakte"""
    return self._breedte * self._hoogte
  def omtrek(self):
    """dit is ee, methode voor de omtrek"""
    return self._breedte + self._breedte + self._hoogte + self._hoogte

  @property
  def hoogte(self):
    """dit is de getter voor de hoogte"""
    return (self._hoogte)

  @hoogte.setter
  def hoogte(self, value):
    """dit is de setter voor de hoogte"""
    if value<0:
      raise ValueError("de waarde kan niet kleiner zijn dan 0")
    else:
      self._hoogte = value

  @property
  def breedte(self):
    """dit is de getter voor de breedte"""
    return (self._breedte)

  @breedte.setter
  def breedte(self, value):
    """dit is de setter voor de breedte"""
    if value<0:
      raise ValueError("de waarde kan niet kleiner zijn dan 0")
    else:
      self._breedte = value

def uitvoeren():
  """deze def is belangrijk omdat we hier in gaan definieren wqat hij straks moet uitvoeren"""
  deur1 = Deur()
  #eerst object aangemaakt

  message = ("de opp van de deur met hoogte {0} en breedte {1} is {2} cm^2")
  message = message.format(deur1.hoogte, deur1.breedte, deur1.oppervlakte())
  print(message)

  message = ("de omtrek van de deur met hoogte {0} en breedte {1} is {2} cm^2")
  message = message.format(deur1.hoogte, deur1.breedte, deur1.omtrek())
  print(message)

  deur2 = Deur(93, 203)
  #tweede object aangemaakt waar we nu de standaardwaarden aanpassen

  message = ("de opp van de deur met hoogte {0} en breedte {1} is {2} cm^2")
  message = message.format(deur2.hoogte, deur2.breedte, deur2.oppervlakte())
  print(message)

  message = ("de omtrek van de deur met hoogte {0} en breedte {1} is {2} cm^2")
  message = message.format(deur2.hoogte, deur2.breedte, deur2.omtrek())
  print(message)


  deur3 = Deur(-10, 203)
  #derde object aangemaakt waar we nu de standaardwaarden aanpassen

  message = ("de opp van de deur met hoogte {0} en breedte {1} is {2} cm^2")
  message = message.format(deur3.hoogte, deur3.breedte, deur3.oppervlakte())
  print(message)

  message = ("de omtrek van de deur met hoogte {0} en breedte {1} is {2} cm^2")
  message = message.format(deur3.hoogte, deur3.breedte, deur3.omtrek())
  print(message)


uitvoeren()

  

  




