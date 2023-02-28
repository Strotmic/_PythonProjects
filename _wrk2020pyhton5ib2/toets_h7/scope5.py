'''Dit is de docstring voor de module'''

a_var = 1

def a_func():
    #a_var = a_var + 1   #hier staat de fout
    print(a_var, '[ a_var inside a_func() ]')

print(a_var, '[ a_var outside a_func() ]')
a_func()


# in regel 6 maak je een fout dat je een niet gedefinieerde lokale variabele a_var 
# een waarde probeert toe te wijzen