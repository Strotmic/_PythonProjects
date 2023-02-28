import pandas as pd
import pyodata
import requests
from requests.auth import HTTPBasicAuth
import xml.etree.cElementTree as et
import json
from MySQLdb import _mysql
from MySQLdb import *
import re

response2 = requests.get(' ',data={'url': 'websiteUrl'}, auth=HTTPBasicAuth('', ' '), stream=True)
#print(response.json())
dic = response2.json()


#33 of 38
test = str(dic["value"][33]["url"])
response = requests.get(f' {test}',data={'url': 'websiteUrl'}, auth=HTTPBasicAuth('', ' '), stream=True)
lengte = len(response.json()['value'])
print(lengte)
types = []
count=0
bad=0

vpl = response.json()["value"]
print(vpl)
for i in range(lengte):
    keys = vpl[i].keys()
    keys = list(keys)
    lengte = (len(vpl[i]))
    if i==0:
        for x in range(lengte):
                types.append(str(type(vpl[i][f"{keys[x]}"])))
    else:
        types2= []
        for x in range(lengte):
                types2.append(str(type(vpl[i][f"{keys[x]}"])))
        if types2==types:
            count+=1
        else: bad+=1

    #for lus om te checken en gelijk te stelen van de lijstne
    if i>0:
        for j in range(lengte):
            een = types[j]
            twee = types2[j]
            if een == "<class 'NoneType'>":
                if twee== "<class 'NoneType'>":
                    pass
                else: types[j] = twee
            else : pass
    

    print(i)




print(types)
print(f'er zijn {count} gelijke en {bad} andere')
print('Finished')