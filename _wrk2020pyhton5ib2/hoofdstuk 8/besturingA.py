from simpleutils.simpledialogs import messagebox, simpledialog



#input 
getal = simpledialog.askinteger("BesturingD", "Geef een getal op")

if getal<=0 :
  messagebox.showerror("BesturingA" , "Het is enkel voor strikt positieve getallen")

else:
  som = 0 
  i = 1
  while i<getal:
    som = som + i
    i = i +1

  #output
  messagebox.showinfo("De som is", str(som))

