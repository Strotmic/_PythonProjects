""" docstring van de module """

#global scope
x=0

def outer():
    #enclosed scope
    x=1
    
    def inner():
        #local scope
        x=2
        print(x)
    inner()

outer()


