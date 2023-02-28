import os
import sys

import mod

print("de directory waar mod gevonden werd is", mod.__file__)
print("=======================================================")

path = os.path.dirname(os.path.abspath(__file__))
print("The current script directory is ", path)

#er moet een omgevingsvariabele PYTHONPATH ingesteld zijn
user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
print("============= alle user_paths======================")

for i in user_paths:
    print(i)


print("============== alle sys paths =====================")

for i in sys.path:
    print(i)
    





