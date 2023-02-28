'''Dit is de docstring voor de module
   Hier zie je dat je ook een instantievariabele 
   dezelfde naam kan geven als een classvariabele
   dit zorgt natuurlijk alleen voor verwarring en dat 
   doe je beter niet!
'''

class Example:
    staticVariable = 5 # Access through class

print(Example.staticVariable) # prints 5

# Access through an instance
instance = Example()
print(instance.staticVariable) # still 5

# Change within an instance
instance.staticVariable = 6
print(instance.staticVariable) # 6
print(Example.staticVariable) # 5

# Change through class
Example.staticVariable = 7
print(instance.staticVariable) # still 6
print(Example.staticVariable) # now 7