'''Dit is de docstring voor de module'''

a_var = 'global variable'

def a_func():
    print(a_var, '[ a_var inside a_func() ]')

a_func()
print(a_var, '[ a_var outside a_func() ]')

# a_var is niet gedefinieerd in de local scope 
# en dus wordt a_var gebruikt uit de global scope