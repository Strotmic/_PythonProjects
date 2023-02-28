'''Dit is de docstring voor de module'''

a_var = 'global value'

def a_func():
    global a_var
    a_var = 'local value'
    print(a_var, '[ a_var inside a_func() ]')

print(a_var, '[ a_var outside a_func() ]')
a_func()
print(a_var, '[ a_var outside a_func() ]')

# met global zorg je ervoor dat a_var wijst naar a_var in de global scope
# met a_var = 'local value' pas je de a_var in de global scope aan