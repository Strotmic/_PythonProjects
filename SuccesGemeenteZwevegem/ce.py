'''import re
def is_spiegelwoord(x):
    pattern ="^[BCDEHIKOX]+$"
    woord = x
    if "None"== str(re.match(pattern,woord)):
        print("False")
    else:
        print("True")

x = "KOOKBOEK"
is_spiegelwoord(x)'''

def som_omgekeerd(x):
    getal= str(x)
    test = ""

    for i in range(len(getal)):
        x = getal[len(getal)-i-1:len(getal)-i]
        test+=x
    test = int(test)
    getal = int(getal)
    som = test + getal

    return som

def is_palindroom(som):
    wel = 0
    som = str(som)
    for i in range(len(som)):
        if len(som)%2 ==0:
            x = som[len(som)-i-1:len(som)-i]
            y = som[i:i+1]
            if x!=y:
                wel+=1
                return False
                break
        else:
            x = som[len(som)-i-1:len(som)-i]
            y = som[i:i+1]
            if x!=y:
                wel +=1
                return False
                break
    if wel==0:
        return True


def g(x,n):
    for i in range(n):

        if is_palindroom(som_omgekeerd(x)) == True:
            return True
        else: 
            print("-----------------------")
            x = som_omgekeerd(x)
            print(x)
    return False
g(377,10)

