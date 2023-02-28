from simpleutils.simpledialogs import messagebox, simpledialog

grootste = 0
getal = 0

for i in range(3):
  i=+1
  getal = simpledialog.askinteger("De grootste ", "geef een getal op")
  if getal>grootste:
    grootste=getal

messagebox.showinfo("De grootste", "Het grootste getal is " + str(grootste))
