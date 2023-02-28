import requests
from requests.auth import HTTPBasicAuth
import json
from MySQLdb import _mysql
from MySQLdb import *
import re
from datetime import datetime
fout=0
succes=0
start = datetime.now()
db = _mysql.connect(user='', password='',
                              host='',
                              database='')
#Haalt de odata files op van het ticket systeem van zwevegem
response2 = requests.get('URL/odata/',data={'url': 'websiteUrl'}, auth=HTTPBasicAuth('Username', 'Password'), stream=True)
#print(response.json())
dic = response2.json()

lengte = len(dic["value"])
foutmelding =[]
for n in range(lengte):
    print(n)
    if n ==300         :
        pass
    else:
        print('ok')
        #doorloopt de urls, dit is gewoon eenkort stukje url
        test = str(dic["value"][n]["url"])
        response = requests.get(f'URL/odata/{test}',data={'url': 'websiteUrl'}, auth=HTTPBasicAuth('Username', 'Password'), stream=True)
        vpl = response.json()["value"]
        #haalt alle values op uit he json value bestand van nr i
        #print(response.json()["value"])

        #berekent hoeveel dict er in de list values zitten van nr i
        lengte2 = len(response.json()["value"])

        if vpl==[]:
                pass
        else:
            #maakt een lege lisjt waar we dan de types zullen insteken van de soorten opgegevne waardees
            types=[]
            keys = vpl[0].keys()
            keys = list(keys)
            lengte = len(vpl)
            count=0
            bad=0
            for p in range(lengte):
                keys = vpl[p].keys()
                keys = list(keys)
                lengte = (len(vpl[p]))
                if p==0:
                    for m in range(lengte):
                            types.append(str(type(vpl[p][f"{keys[m]}"])))
                else:
                    types2= []
                    for k in range(lengte):
                            types2.append(str(type(vpl[p][f"{keys[k]}"])))
                    if types2==types:
                        count+=1
                    else: bad+=1

                #for lus om te checken en gelijk te stelen van de lijstne
                if p>0:
                    for j in range(lengte):
                        een = types[j]
                        twee = types2[j]
                        if een == "<class 'NoneType'>":
                            if twee== "<class 'NoneType'>":
                                pass
                            else: types[j] = twee
                        else : pass

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
                        pass
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
                                pass
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
                                pass
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
                                pass
                            elif "bool" in types[i]:
                                toevoeg += f"{keys[i]}, "
                                nummers+=1
                            elif "float" in types[i]:
                                toevoeg += f"{keys[i]}, "
                                nummers+=1
                            else:
                                pass
            toevoeg = toevoeg[:- 2]     
            toevoeg +=")"      
            toevoeg += " values("  
            
            #drukt alle id's af
            vpl = response.json()["value"]
            for j in range(lengte2):
                toevoeg2 = toevoeg
                nummesr2=0
                for o in range(len(keys)):
                    #print(f"{nummers} en {nummesr2} en lengte {len(keys)} lengte is {len(vpl[j])} \n \n en de keys zijn {vpl[j]} \n \n en types {types} \n \n")
                    
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
                       
                        if "None" in str(type(vpl[j][f"{keys[o]}"])):
                                if 'None' in types[o]:
                                    pass
                                else:
                                    if 'str' in types[o]:
                                        toevoeg2 += f"'Empty', "
                                        nummesr2+=1
                                    elif "bool" in types[o]:
                                        toevoeg2 += f'False, '
                                        nummesr2+=1
                                    elif "int" in types[o]:
                                        toevoeg2 += f"0, "
                                        nummesr2+=1
                                    elif "float" in types[o]:
                                        toevoeg2 += f"0, "
                                        nummesr2+=1
                                    


                        elif "str" in str(type(vpl[j][f"{keys[o]}"])):
                            #print de value van de key in keys van de i'de dict
                                vpl[j][f"{keys[o]}"]
                                vpl[j][f'{keys[o]}'] = re.sub("[']", " ", vpl[j][f'{keys[o]}'])
                                try:
                                    vpl[j][f'{keys[o]}'] = vpl[j][f'{keys[o]}'].replace("\\","/")
                                except:
                                    pass
                                toevoeg2 += f"'{vpl[j][f'{keys[o]}']}', "
                                nummesr2+=1
                        elif "bool" in str(type(vpl[j][f"{keys[o]}"])):
                                if "True" in str(vpl[j][f"{keys[o]}"]):
                                    toevoeg2 += f'True, '
                                    nummesr2+=1
                                else:
                                    toevoeg2 += f'False, '
                                    nummesr2+=1
                        else:
                                #print de value van de key in keys van de i'de dict
                                toevoeg2 += f'{vpl[j][f"{keys[o]}"]}, '
                                nummesr2+=1

                toevoeg2 = toevoeg2[:- 2]     
                toevoeg2 +=")"     
                try:
                    db.query(toevoeg2)
                    succes+=1
                except:
                    fout+=1
                    foutmelding.append(toevoeg2)
                    print(f"{toevoeg2}----------------")

print(f'de starttijd was {start}')
now = datetime.now()
print(foutmelding)
print(f"het is gedaan {succes} succesvolle en {fout} foutieve")
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
            
