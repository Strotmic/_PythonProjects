from simpleutils.simpledialogs import messagebox, simpledialog
from mijnPackageh4.teller import Teller



teller = Teller()
teller.tellerstaataan = True


while True:

  #input
  getal = simpledialog.askinteger("Simpeltellen" , "geef een geheel getal op")

  for i in range(getal):
    teller.increment()

  #output
  messagebox.showinfo("Simpeltellen", "de teller staat op " + str(teller.waarde))
  
  if getal==0:
    break

