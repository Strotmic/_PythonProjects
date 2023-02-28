
from random import seed
from random import randint
from random import uniform
from random import randrange

def uitvoeren():
  random = randint(0,100)
  print("het geheel getal met random.randint(0,100)" , random)

  random = randrange(101)
  print("het geheel getal met random.randint(101):", random)

  random = uniform(0,100)
  print("het komma getal met random.randint(0,100):", random)
  print("het komma getal met random.randint(0,100):", round(random, 2))




  
uitvoeren()





