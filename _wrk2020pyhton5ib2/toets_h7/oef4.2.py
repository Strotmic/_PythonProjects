from simpleutils.simpledialogs import messagebox, simpledialog


class Driehoek:
  def __init__(self, basis=0, hoogte=0):
    self.basis = simpledialog.askinteger("Basis", "Geef een basis op")
    self.hoogte = simpledialog.askinteger("Hoogte", "Geef een hoogte op")

  def oppervlakte(self):
    return messagebox.showinfo("De oppervlakte is", (self.basis * self.hoogte)/2)

  @property
  def basis(self):
    return (self._basis)

  @basis.setter
  def basis(self, value):
    if value<0:
      messagebox.showinfo("Error", "de waarde mag niet kleiner zijn dan 0")
    else:
      self._basis = value

  @property
  def hoogte(self):
    return (self._hoogte)

  @hoogte.setter
  def hoogte(self, value):
    if value<0:
      messagebox.showinfo("Error", "de waarde mag niet kleiner zijn dan 0")
    else:
      self._hoogte = value


def uitvoeren():
  x = Driehoek()
  x.oppervlakte()
  

uitvoeren()