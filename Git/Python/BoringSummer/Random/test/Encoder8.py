'''
In this docuemnt i will make a program to autmake code
'''

import ast
import re

with open('.env.txt') as f:
    lines = f.readlines()

message= input()

with open('dic/alphabet.txt') as f:
    data = f.read()
d = ast.literal_eval(data)

lijst = list(message)
k=0

for i in lijst:

    for j in d.values():
        if i==j:
            for n in d.keys():
                if d[n] == j:
                    lijst[k] = n * int(lines[0])
                    k +=1
    

print(lijst)


#decoder

k=0
for i in lijst:
    lijst[k] = int(i / int(lines[0]))
    k+=1

k=0
antwoord = ''
for g in lijst:
    for o in d.keys():
        if o == g:
            antwoord += d[o]
            k+=1
print(antwoord)