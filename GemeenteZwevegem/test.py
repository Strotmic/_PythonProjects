from MySQLdb import _mysql
from MySQLdb import *
import pandas as pd
from pandas import DataFrame
from django.db import connection
import re

db = _mysql.connect(user='root', password='Gusco10.+789',
                              host='127.0.0.1',
                              database='gemeente')


df = pd.read_excel('Map1.xlsx')
print(df)


lengte = int(df.shape[0])


for i in range(lengte):
    voorlopig = list(df.loc[i])
    id = int(voorlopig[0])
    gebruiker = str(voorlopig[1])
    gebruiker = re.sub("[']"," ",gebruiker)
    kaart = str(voorlopig[2])
    hostnaam = str(voorlopig[3])
    serienummer = str(voorlopig[4])
    objec = str(voorlopig[5])
    merk = str(voorlopig[6])
    soort = str(voorlopig[7])
    specificatie = str(voorlopig[8])
    vestiging = str(voorlopig[9])
    status = str(voorlopig[10])
    lokaal = str(voorlopig[11])
    ordernummer=str(voorlopig[12])
    ipadres = str(voorlopig[13])
    aantekeningen = str(voorlopig[14])
    aantekeningen = re.sub("[‰']","",aantekeningen)
    if status == "Non Actief":
        pass
    else :db.query(f"insert into lijstgemeente(id,serienummer,gebruiker,kaart,hostnaam,object,merk,soort,specificatie,vestiging,stats,lokaal,ordernummer,ipadres,aantekening) values({id},'{serienummer}','{gebruiker}','{kaart}','{hostnaam}','{objec}','{merk}','{soort}','{specificatie}','{vestiging}','{status}','{lokaal}','{ordernummer}','{ipadres}','{aantekeningen}')")


print("----------------------------------")

db.query("select * from lijstgemeente where object='LAP0250'")
q = db.store_result()
q = q.fetch_row()
q = str(q)
q = re.sub("'()"," ",str(q))
print(q)








