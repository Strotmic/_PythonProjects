import pandas as pd
import pyodata
import requests
from requests.auth import HTTPBasicAuth
import xml.etree.cElementTree as et
import json
from MySQLdb import _mysql
from MySQLdb import *
import re

db = _mysql.connect(user='root', password='Gusco10.+789',
                              host='127.0.0.1',
                              database='odata')

#Haalt de odata files op van het ticket systeem van zwevegem
response2 = requests.get('',data={'url': 'websiteUrl'}, auth=HTTPBasicAuth('', ' '), stream=True)
#print(response.json())
dic = response2.json()


#open t een nieuwe url met als extra parameter 'value', dat is een lijst van dictionaries met alle namen van de tabellen en hun url
response3 = requests.get(f'{dic["value"]}',data={'url': 'websiteUrl'}, auth=HTTPBasicAuth('', ' '), stream=True)

lengte = len(dic["value"])
for i in range(lengte):
    print(f'{i} + {str(dic["value"][i]["url"])}')

test = str(dic["value"][38]["url"])

#geeft de test parameter mee in het url waardoor de odata geladen word van de opgevraagde parameter
response = requests.get(f'{test}',data={'url': 'websiteUrl'}, auth=HTTPBasicAuth('', ' '), stream=True)
print(response.json())

