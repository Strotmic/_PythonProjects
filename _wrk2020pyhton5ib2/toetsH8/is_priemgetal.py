from simpleutils.simpledialogs import messagebox, simpledialog

def priem():
    #invoer
    while True:
        getal = simpledialog.askinteger("Simpeltellen" , "geef een geheel getal op groter dan 1")

        #eens je een getal hebt mag deze loop stoppen
        if getal >1:
            break
            

    delers = " "

    #verwerking
    priem = 0
    for i in range(getal):
        i+=1
    
        if getal%i==0:
        
        
            delers = "" + delers + str(i) + ", "

            priem +=i


    delers = delers[:-2]

    #uitvoer
    if priem == getal + 1:
        messagebox.showinfo("delers", "het is een priemgetal want de delers zijn" + str(delers))

    #geen priemgetal omdat het te veel delers heeft
    else:
        messagebox.showerror("delers", "het is geen priemgetal want de delers zijn:" + str(delers))

priem()