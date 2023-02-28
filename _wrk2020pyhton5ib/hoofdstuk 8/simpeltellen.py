from simpleutils.simpledialogs import messagebox, simpledialog
from mijnPackageh4.teller import Teller

#input
getal = simpledialog.askinteger("Simpeltellen" , "geef een geheel getal op")

teller = Teller()
teller.tellerstaataan = True

for i in range(getal):
  teller.increment()

#output
messagebox.showinfo("Simpeltellen", "de teller staat op " + str(teller.waarde)) 

