from tkinter.constants import X
from simpleutils.simpledialogs import simpledialog
import random

x= simpledialog

steen = 'steen'
blad = 'blad'
schaar = 'schaar'

bot = random.randrange(0,2)
botres = ''

if(bot==0):
    botres = steen
elif(bot==1):
    botres = schaar
elif(bot==2):
    botres = blad


persoon = x.askstring('Blad steen schaar', 'Wat is uw keuze')

while persoon==botres:
    persoon = x.askstring('Blad steen schaar', 'Wat is uw keuze')
    bot = random.randrange(0,2)
    if(bot==0):
        botres = steen
    elif(bot==1):
        botres = schaar
    elif(bot==2):
        botres = blad

if(botres==steen and persoon ==blad):
    print('You won, your choice ' + str(persoon) + ' de bot choise ' + str(botres))

if(botres==blad and persoon ==schaar):
    print('You won, your choice ' + str(persoon) + ' de bot choise ' + str(botres))

if(botres==schaar and persoon ==steen):
    print('You won, your choice ' + str(persoon) + ' de bot choise ' + str(botres))
    
if(persoon==steen and botres ==blad):
    print('You lost, your choice ' + str(persoon) + ' de bot choise ' + str(botres))

if(persoon==blad and botres ==schaar):
    print('You lost, your choice ' + str(persoon) + ' de bot choise ' + str(botres))

if(persoon==schaar and botres ==steen):
    print('You lost, your choice ' + str(persoon) + ' de bot choise ' + str(botres))
