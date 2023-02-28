from functools import total_ordering
from MySQLdb import _mysql
from MySQLdb import *
from numpy import full
import pandas as pd
from pandas import DataFrame
from django.db import connection
import re


db = _mysql.connect(user='root', password='Gusco10.+789',
                              host='127.0.0.1',
                              database='gemeente')

db.query("create table if not exists gebruikers_nu(id integer primary key, pad varchar(1000))")

prijs2022 = 250000
prijs2019 = 180000
#---------------------------------------------------------------------------------------------------------
df = pd.read_excel('grafiek.xlsx')



lijst=[]
lijst3=[]
lengte = int(df.shape[0])

for i in range(lengte):
    voorlopig = list(df.loc[i])
    gebruiker = str(voorlopig[9])
    mail = str(voorlopig[28])
    if "Gebruiker" in gebruiker:       
        mail2 = re.sub("^[^_]*@","",mail)
        if "ocmw" in mail2:
            lijst.append(gebruiker)
        elif mail2== "zwevegem.be":
            lijst.append(gebruiker)
        else:
            lijst3.append(gebruiker)
    else: pass

#---------------------------------------------------------------------------------------------------------
lijst2=[]

df = pd.read_excel('grafiek2.xlsx')
lengte2 = int(df.shape[0])
for i in range(lengte2):
    voorlopig = list(df.loc[i])
    gebruiker = str(voorlopig[9])
    if "Gebruiker" in gebruiker:
        lijst2.append(gebruiker)
    else: pass

#---------------------------------------------------------------------------------------------------------
df = pd.read_excel('grafiek.xlsx')

df2 = pd.read_excel('...')  #deze gaan we morgen de uren inlezen

uren=[]
fulltimes = []
parttime = []
urenfull = 0
urenpart = 0

lengte3 = int(df.shape[0])  #hier zullen we de langste lijst moetne inzetten, normaal komt deze overeen
lengte4 = int(df2.shape[0])   

for i in range(lengte3):
    voorlopig1 = list(df.loc[i])
    mail = str(voorlopig1[28])
    for j in range(lengte4):
        voorlopig2 = list(df2.loc[j])
        mail2 = str(voorlopig2[0]) # mail van het andere excel document het nummer
        if mail == mail2:
            starttijd = str(voorlopig2[0]) # rij van start uur  kan zijn dat er meerder dagen zijn dan moeten we voor elk start uur en eind uur een andere parameter maken
            einduur = str(voorlopig2[0])
            totaaluur = einduur - starttijd
            if totaaluur == 37: # aantal uren van een fultime
                fulltimes.append(mail2)
                urenfull +=totaaluur
            else:
                parttime.append(mail2)
                urenpart +=totaaluur 
                
        


            combo = totaaluur + mail2
            uren.append(combo)

totaal = len(fulltimes)+len(parttime)  # berekent totaal aantal mense
procentfull = len(fulltimes)/totaal  # hoeveel procent van mensen die fulltime werkt
procentpart = len(parttime)/totaal # hoeveel procent van mensen die parttime werkt

prijsfull = totaal * procentfull # de totale prijs van alle fulltimers
prijspart = totaal * procentpart # de totale prijs van parttimers

print(f"de totaal prijs voor full timers zijn {prijsfull}")
print(f"de totaal prijs voor part timers zijn {prijspart}")
print(f"alle full time uren {urenfull} en {len(fulltimes)} mensen werken fulltime")
print(f"alle full time uren {urenpart} en {len(parttime)} mensen werken fulltime")
#---------------------------------------------------------------------------------------------------------
print("--------------------------------------------")
print(f"er zijn {len(lijst)} mensen met email zwevegem.be of ocmw.zwevegem.be")
print(f"er zijn {len(lijst3)} mensen met andere emails (vooral onderwijs)")
een = len(lijst)+len(lijst3)
print(f"in het totaal zijn er {een} users \n")
print(f"er waren {str(len(lijst2))} mensen in 2019 \n")
twee = len(lijst2)

#---------------------------------------------------------------------------------------------------------
print("Procentuele verandering ")
drie = een - twee
print(f"er is een verschil van {drie} mensen tussen nu en 2019")
procent = drie / twee
print(f"er is een stijging van {procent*100} procent tussen 2019 en 2022")

#---------------------------------------------------------------------------------------------------------







