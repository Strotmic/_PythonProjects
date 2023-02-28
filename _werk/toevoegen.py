import pandas as pd
import pyodata
import requests
from requests.auth import HTTPBasicAuth
import xml.etree.cElementTree as et
import json
from MySQLdb import _mysql
from MySQLdb import *
import re
from datetime import datetime
fout=0
succes=0

db = _mysql.connect(user='root', password='Gusco10.+789',
                              host='127.0.0.1',
                              database='odata')

#Haalt de odata files op van het ticket systeem van zwevegem
response2 = requests.get(' ',data={'url': 'websiteUrl'}, auth=HTTPBasicAuth('', ' '), stream=True)
#print(response.json())
dic = response2.json()

lengte = len(dic["value"])
for n in range(lengte):
    print(n)
    if n ==33:
        pass
    else:
        #doorloopt de urls, dit is gewoon eenkort stukje url
        test = str(dic["value"][n]["url"])
        response = requests.get(f' {test}',data={'url': 'websiteUrl'}, auth=HTTPBasicAuth('', ' '), stream=True)

        #haalt alle values op uit he json value bestand van nr i
        #print(response.json()["value"])

        #berekent hoeveel dict er in de list values zitten van nr i
        lengte2 = len(response.json()["value"])

        if response.json()["value"]==[]:
                pass
        else:
            #maakt een lege lisjt waar we dan de types zullen insteken van de soorten opgegevne waardees
            types=[]
            keys = response.json()["value"][0].keys()
            keys = list(keys)
            
            for x in range(len(keys)):
                response.json()["value"][0]
                types.append(str(type(response.json()["value"][0][f"{keys[x]}"])))
            print(types)
            db.query(f'truncate table {dic["value"][n]["url"]}')
            toevoeg = f'insert into {dic["value"][n]["url"]}('
            nummers = 0
            for i in range(len(keys)):
                if keys[i] == "status":
                    keys[i] = "statuss"
                    keys[i] = re.sub("[']", "'", keys[i])

                    if "str" in types[i]:
                        toevoeg += f"{keys[i]}, "
                        nummers+=1
                    elif "int" in types[i]:
                        toevoeg += f"{keys[i]}, "
                        nummers+=1
                    elif "NoneType" in types[i]:
                        toevoeg += f"{keys[i]}, "
                        nummers+=1
                    elif "bool" in types[i]:
                        toevoeg += f"{keys[i]}, "
                        nummers+=1
                    elif "float" in types[i]:
                        toevoeg += f"{keys[i]}, "
                        nummers+=1
                    else:
                        pass
                else:
                    if keys[i] == "order":
                            keys[i] = "orde"
                            keys[i] = re.sub("[']", "'", keys[i])
                            keys[i] = re.sub("[']", "'", keys[i])
                            if "str" in types[i]:
                                toevoeg += f"{keys[i]}, "
                                nummers+=1
                            elif "int" in types[i]:
                                toevoeg += f"{keys[i]}, "
                                nummers+=1
                            elif "NoneType" in types[i]:
                                toevoeg += f"{keys[i]}, "
                                nummers+=1
                            elif "bool" in types[i]:
                                toevoeg += f"{keys[i]}, "
                                nummers+=1
                            elif "float" in types[i]:
                                toevoeg += f"{keys[i]}, "
                                nummers+=1
                            else:
                                pass
                    else:
                        if keys[i]=="by" :
                            keys[i] = "bye"
                            if "str" in types[i]:
                                toevoeg += f"{keys[i]}, "
                                nummers+=1
                            elif "int" in types[i]:
                                toevoeg += f"{keys[i]}, "
                                nummers+=1
                            elif "NoneType" in types[i]:
                                toevoeg += f"{keys[i]}, "
                                nummers+=1
                            elif "bool" in types[i]:
                                toevoeg += f"{keys[i]}, "
                                nummers+=1
                            elif "float" in types[i]:
                                toevoeg += f"{keys[i]}, "
                                nummers+=1
                            else:
                                pass

                        else:
                            if "str" in types[i]:
                                toevoeg += f"{keys[i]}, "
                                nummers+=1
                            elif "int" in types[i]:
                                toevoeg += f"{keys[i]}, "
                                nummers+=1
                            elif "NoneType" in types[i]:
                                toevoeg += f"{keys[i]}, "
                                nummers+=1
                            elif "bool" in types[i]:
                                toevoeg += f"{keys[i]}, "
                                nummers+=1
                            elif "float" in types[i]:
                                toevoeg += f"{keys[i]}, "
                                nummers+=1
                            else:
                                pass
            print(nummers)
            toevoeg = toevoeg[:- 2]     
            toevoeg +=")"      
            toevoeg += " values("  
            
            #drukt alle id's af
            for j in range(lengte2):
                toevoeg2 = toevoeg
                nummesr2=0
                for o in range(len(keys)):
                    if nummesr2==nummers:
                        break
                    else:
                        if keys[o] == 'statuss':
                            keys[o] = 'status'
                        if keys[o] == 'orde':
                            keys[o] = 'order' 
                        if keys[o] == 'bye':
                            keys[o] = 'by'                                                        
                        #checked of het antwoord niet none is
                       
                        if "str" or "None" in str(type(response.json()["value"][j][f"{keys[o]}"])):
                                #print de value van de key in keys van de i'de dict
                                response.json()["value"][j][f"{keys[o]}"]
                                toevoeg2 += f'"{response.json()["value"][j][f"{keys[o]}"]}", '
                                nummesr2+=1

                        else:
                                #print de value van de key in keys van de i'de dict
                                print(response.json()["value"][j][f"{keys[o]}"])
                                toevoeg2 += f'{response.json()["value"][j][f"{keys[o]}"]}, '
                                nummesr2+=1

                toevoeg2 = toevoeg2[:- 2]     
                toevoeg2 +=")"     
                print(toevoeg2)
                try:
                    db.query(toevoeg2)
                    print("------------------------------------------------------")
                    succes+=1
                except:
                    fout+=1

print(f"het is gedaan {succes} succesvolle en {fout} foutieve")
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
            
