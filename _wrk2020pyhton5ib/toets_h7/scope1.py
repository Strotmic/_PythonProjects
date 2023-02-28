'''Dit is de docstring voor de module'''
#print(globals()) # prints global namespace
#print(locals()) # prints local namespace

glob = 1
glob2 = 4

def een_functie():
    loc = 5
    loc2 = 6
    print("een lijst met de locals", locals())
    print('is loc lokaal in een_functie:', 'loc' in locals())

een_functie()
print('is loc een global?', 'loc' in globals())
print('is glob een global?', 'glob' in globals())
print('is een_functie een global?', 'een_functie' in globals())
print("een lijst met de globals", globals())
print("een lijst met de locals", locals())
