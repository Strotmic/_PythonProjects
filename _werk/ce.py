getal = "227"
test =" "
wel= 0
for i in range(len(getal)):
    x = getal[len(getal)-i-1:len(getal)-i]
    test+=x

test = int(test)
getal = int(getal)
som = test + getal
print(som)
som = str(som)
for i in range(len(som)):
    if len(som)%2 ==0:
        x = som[len(som)-i-1:len(som)-i]
        y = som[i:i+1]
        if x!=y:
            wel+=1
            print("geen palingsyndroom")
            break
    else:
        x = som[len(som)-i-1:len(som)-i]
        y = som[i:i+1]
        if x!=y:
            wel +=1
            print("geen palingsyndroom")
            break
if wel==0:

    print("wel palingstndroom")

        




