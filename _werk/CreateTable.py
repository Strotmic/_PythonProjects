import pandas as pd
import pyodata
import requests
from requests.auth import HTTPBasicAuth
import xml.etree.cElementTree as et
import json
from MySQLdb import _mysql
from MySQLdb import *
import re

succesvol = 0
fout = 0
db = _mysql.connect(user='root', password='Gusco10.+789',
                              host='127.0.0.1',
                              database='odata')

#Haalt de odata files op van het ticket systeem van zwevegem
response2 = requests.get(' ',data={'url': 'websiteUrl'}, auth=HTTPBasicAuth('', ''), stream=True)
#print(response.json())
dic = response2.json()


'''#open t een nieuwe url met als extra parameter 'value', dat is een lijst van dictionaries met alle namen van de tabellen en hun url
response3 = requests.get(f' {dic["value"]}',data={'url': 'websiteUrl'}, auth=HTTPBasicAuth('', ' '), stream=True)
'''
#berektn de lengte van hoeveel tabbelen er zijn en print deze daarna uit met hun bijbehoorende id
lengte2 = len(dic["value"])
for i in range(lengte2):
    test = str(dic["value"][i]["url"])

print(lengte2)
print()
for j in range(lengte2):
    print(j)
    #haalt het url op van value i en stopt dit in de parameter test
    test = str(dic["value"][j]["url"])

    #geeft de test parameter mee in het url waardoor de odata geladen word van de opgevraagde parameter
    response = requests.get(f' {test}',data={'url': 'websiteUrl'}, auth=HTTPBasicAuth('', ' '), stream=True)

    #berekent de lengte van het key value paren in de dictionary
    if response.json()["value"] != []:
        lengte = len(response.json()["value"][0])

         #maken een lege list aan voor de types die we later zullen gebruiken
        types = []

        #berekent alle keys van de dictionary en steekt deze in een list
        keys = response.json()["value"][0].keys()
        keys = list(keys)

        #overloopt een voor een de waardes in de dictionary en stopt de type van de waarden in een list types
        for x in range(lengte):
            response.json()["value"][0]
            types.append(str(type(response.json()["value"][0][f"{keys[x]}"])))

        print(type(keys[1]))
        #hier maken we op basis van de lengte en van de types list een sql anotatie om een gepaste tabel te creeren
        sqlstring = f'create table if not exists {dic["value"][j]["url"]}('
        for i in range(lengte):  
            #alle kesy die status als naam hebben moeten worden aangepast naar statuss omdat status niet mag in sql
            if keys[i] == "status":
                keys[i] = "statuss"
                keys[i] = re.sub("[']", "'", keys[i])
                #we checken of de key 'id' is, zo ja zullen we deze gebruiken als primary key
                if keys[i]=="Id" or keys[i]=="id":
                            if "str" in types[i]:
                                sqlstring += f"{keys[i]} varchar(100) primary key not null, "
                            elif "int" in types[i]:
                                sqlstring+= f"{keys[i]} integer primary key not null, "
                            elif "NoneType" in types[i]:
                                pass
                            elif "bool" in types[i]:
                                sqlstring += f"{keys[i]} boolean primary key not null, "
                            elif "float" in types[i]:
                                sqlstring += f"{keys[i]} float primary key not null, "
                            else:
                                pass
                else:             
                            if "str" in types[i]:
                                sqlstring += f"{keys[i]} varchar(100), "
                            elif "int" in types[i]:
                                sqlstring+= f"{keys[i]} integer, "
                            elif "NoneType" in types[i]:
                                sqlstring += f"{keys[i]} varchar(100), "
                            elif "bool" in types[i]:
                                sqlstring += f"{keys[i]} boolean, "
                            elif "float" in types[i]:
                                sqlstring += f"{keys[i]} float, "
                            else:
                                sqlstring += f"{keys[i]} varchar(100), "
            #---------------------------------------------------------------------------------------------    
            else:
                #alle kesy die order als naam hebben moeten worden aangepast naar orde omdat order niet mag in sql
                if keys[i] == "order":
                        keys[i] = "orde"
                        keys[i] = re.sub("[']", "'", keys[i])
                        keys[i] = re.sub("[']", "'", keys[i])
                        if keys[i]=="Id" or keys[i]=="id":
                                    if "str" in types[i]:
                                        sqlstring += f"{keys[i]} varchar(100) primary key not null, "
                                    elif "int" in types[i]:
                                        sqlstring+= f"{keys[i]} integer primary key not null, "
                                    elif "NoneType" in types[i]:
                                        pass
                                    elif "bool" in types[i]:
                                        sqlstring += f"{keys[i]} boolean primary key not null, "
                                    elif "float" in types[i]:
                                        sqlstring += f"{keys[i]} float primary key not null, "
                                    else:
                                        sqlstring += f"{keys[i]} varchar(100) primary key not null, "
                        else:             
                                    if "str" in types[i]:
                                        sqlstring += f"{keys[i]} varchar(100), "
                                    elif "int" in types[i]:
                                        sqlstring+= f"{keys[i]} integer, "
                                    elif "NoneType" in types[i]:
                                        sqlstring += f"{keys[i]} varchar(100), "
                                    elif "bool" in types[i]:
                                        sqlstring += f"{keys[i]} boolean, "
                                    elif "float" in types[i]:
                                        sqlstring += f"{keys[i]} float, "
                                    else:
                                        sqlstring += f"{keys[i]} varchar(100), "
                else:
                    if keys[i]=="by" :
                        keys[i] = "bye"
                        if keys[i]=="Id" or keys[i]=="id":
                                    if "str" in types[i]:
                                        sqlstring += f"{keys[i]} varchar(100) primary key not null, "
                                    elif "int" in types[i]:
                                        sqlstring+= f"{keys[i]} integer primary key not null, "
                                    elif "NoneType" in types[i]:
                                        sqlstring += f"{keys[i]} varchar(100) primary key not null, "
                                    elif "bool" in types[i]:
                                        sqlstring += f"{keys[i]} boolean primary key not null, "
                                    elif "float" in types[i]:
                                        sqlstring += f"{keys[i]} float primary key not null, "
                                    else:
                                        sqlstring += f"{keys[i]} varchar(100) primary key not null, "
                        else:             
                                    if "str" in types[i]:
                                        sqlstring += f"{keys[i]} varchar(100), "
                                    elif "int" in types[i]:
                                        sqlstring+= f"{keys[i]} integer, "
                                    elif "NoneType" in types[i]:
                                        sqlstring += f"{keys[i]} varchar(100) ,"
                                    elif "bool" in types[i]:
                                        sqlstring += f"{keys[i]} boolean, "
                                    elif "float" in types[i]:
                                        sqlstring += f"{keys[i]} float, "
                                    else:
                                        sqlstring += f"{keys[i]} varchar(100), "
                    else:             
                            if keys[i]=="Id" or keys[i]=="id":
                                    if "str" in types[i]:
                                        sqlstring += f"{keys[i]} varchar(100) primary key not null, "
                                    elif "int" in types[i]:
                                        sqlstring+= f"{keys[i]} integer primary key not null, "
                                    elif "NoneType" in types[i]:
                                        sqlstring += f"{keys[i]} varchar(100), "
                                    elif "bool" in types[i]:
                                        sqlstring += f"{keys[i]} boolean primary key not null, "
                                    elif "float" in types[i]:
                                        sqlstring += f"{keys[i]} float primary key not null, "
                                    else:
                                        sqlstring += f"{keys[i]} varchar(100), "
                            else:             
                                    if "str" in types[i]:
                                        sqlstring += f"{keys[i]} varchar(100), "
                                    elif "int" in types[i]:
                                        sqlstring+= f"{keys[i]} integer, "
                                    elif "NoneType" in types[i]:
                                        sqlstring += f"{keys[i]} varchar(100), "
                                    elif "bool" in types[i]:
                                        sqlstring += f"{keys[i]} boolean, "
                                    elif "float" in types[i]:
                                        sqlstring += f"{keys[i]} float, "
                                    else:
                                        sqlstring += f"{keys[i]} varchar(100), "

        #we verminderen de string met 2 zodat de witruimte en laatste komma weg is en zetten een haakje
        sqlstring = sqlstring[:- 2]     
        sqlstring +=")"                       
        print(sqlstring)
        
        #we proberen de tabel te creeeren en printen dan af of dit gelukt is of niet
        try:
            db.query(sqlstring)
            print(f'Goed toegevoegd + {dic["value"][j]["url"]}')
            succesvol +=1
        except:
                print(f"fout bij {i} +  {keys[j]}")
                print("--")
                fout +=1
        print("--")                                


        '''
        Hier moet code komen om dan de databases te vullen eens al de tabellen succesvol gemaakt zijn

        Later zullen we ook nog kijken voor foreign keys te assignen

        '''


    else:
        pass



#als alles klaar is printen we finished om te laten weten dat het succesvol gelukt is zonder al te veel fouten en printen we de counter af van foutmeldingen
print("Finished")
print(f'Er zijn {succesvol} tebellen correcet ingevoerd en er waren {fout} fouten')



