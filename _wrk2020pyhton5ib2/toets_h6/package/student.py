#nieuwe klasse genaamd student
class Student:

  def __init__(self, naam="Jan", gewicht=0):
    self.naam = naam
    self.gewicht = gewicht
    #constructor met als properties naam en gewicht
  def snoepen(self):
    self.gewicht += 0.5
  """methode snoepen die gewicht +0.5 doet"""

  def studeren(self):
    self.gewicht -= 0.5
  #methode studeren die gewicht -0.5 doet
  
  """geen property decorater omdat er staat dat er geen controle moet toegekent worden zowel bij opvragen als instellen"""

