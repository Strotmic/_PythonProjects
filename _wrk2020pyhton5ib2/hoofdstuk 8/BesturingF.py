from simpleutils.simpledialogs import messagebox, simpledialog


while True:
   getal = simpledialog.askinteger("Simpeltellen" , "geef een geheel getal op")

   if getal >0:
     break
delers = "De delers zijn : "

for i in range(getal):
  i+=1
  
  if getal%i==0:
    
    
    delers = "" + delers + str(i) + ", "
   

delers = delers[:-2]
messagebox.showinfo("delers", delers)
    
    
  
    

