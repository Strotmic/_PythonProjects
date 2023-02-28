'''Dit is de docstring voor de module'''

a_var = 'global value'

def outer():
       a_var = 'local value'
       print('outer before:', a_var)
       def inner():
           nonlocal a_var
           a_var = 'inner value'
           print('in inner():', a_var)
       inner()
       print("outer after:", a_var)
outer()


# met nonlocal geef je aan dat a_var geen lokale variabele is 
# maar dat moet gekeken worden in de enclosed space
# met de regel na nonlocal a_var wordt dus de variabele a_var in de enclosed space aangepast
# dit is a_var gedefinieerd in outer()