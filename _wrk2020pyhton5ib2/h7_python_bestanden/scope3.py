'''Dit is de docstring voor de module'''

a_var = 'global value'

def a_func():
    a_var = 'local value'
    print(a_var, '[ a_var inside a_func() ]')

a_func()
print(a_var, '[ a_var outside a_func() ]')

# a_var is wel gedefinieerd in de local scope 
# en dus wordt a_var gebruikt uit de local scope
# en niet uit de global scope