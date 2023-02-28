from django.db import models
from django.db import connection
import mysql.connector
import pandas as pd
from pandas import DataFrame
import re

mysql.connector.connect(user='root', password='Gusco10.+789',
                              host='127.0.0.1',
                              database='gemeente')

con = connection.cursor()

#een constructor voor een klasse persoon 
class persoon(models.Model):
    def __init__(self,id,serienummer,gebruiker,kaart,hostnaam,object,merk,soort,specificatie,vestiging,status,lokaal,ordernummer,ipadres,aantekening):
        self.id = id
        self.serienummer = serienummer
        self.gebruiker = gebruiker
        self.kaart = kaart
        self.hostnaam = hostnaam
        self.object = object
        self.merk = merk
        self.soort = soort
        self.specificatie = specificatie
        self.vestiging = vestiging
        self.status = status
        self.lokaal =lokaal
        self.ordernummer = ordernummer
        self.ipadres = ipadres
        self.aantekening = aantekening

#maakt een lijst users met alle users die in het excel document staan
def getUser():
    df = pd.read_excel('../Map1.xlsx')
    lengte = int(df.shape[0])
    users = []
    
    for i in range(lengte):
        voorlopig = list(df.loc[i])
        id = i+1
        gebruiker = str(voorlopig[0])
        gebruiker = re.sub("[']"," ",gebruiker)
        kaart = str(voorlopig[1])
        hostnaam = str(voorlopig[2])
        serienummer = str(voorlopig[3])
        objec = str(voorlopig[4])
        merk = str(voorlopig[5])
        soort = str(voorlopig[6])
        specificatie = str(voorlopig[7])
        vestiging = str(voorlopig[8])
        status = str(voorlopig[9])
        lokaal = str(voorlopig[10])
        ordernummer=str(voorlopig[11])
        ipadres = str(voorlopig[12])
        aantekeningen = str(voorlopig[13])
        aantekeningen = re.sub("[‰']","",aantekeningen)
        if status == "Non Actief":
            pass
        else :
            users.append( persoon(id,serienummer,gebruiker,kaart,hostnaam,objec,merk,soort,specificatie,vestiging,status,lokaal,ordernummer,ipadres,aantekeningen))
    return users


#dient om de lijst aan te maken als deze nog niet bestaat
def update(): 
    df = pd.read_excel('../Map1.xlsx')

    lengte = int(df.shape[0])

    for i in range(lengte):
        voorlopig = list(df.loc[i])
        id = i+1
        gebruiker = str(voorlopig[0])
        gebruiker = re.sub("[']"," ",gebruiker)
        kaart = str(voorlopig[1])
        hostnaam = str(voorlopig[2])
        serienummer = str(voorlopig[3])
        objec = str(voorlopig[4])
        merk = str(voorlopig[5])
        soort = str(voorlopig[6])
        specificatie = str(voorlopig[7])
        vestiging = str(voorlopig[8])
        status = str(voorlopig[9])
        lokaal = str(voorlopig[10])
        ordernummer=str(voorlopig[11])
        ipadres = str(voorlopig[12])
        aantekeningen = str(voorlopig[13])
        aantekeningen = re.sub("[‰']","",aantekeningen)
        if status == "Non Actief":
            pass
        else :con.execute(f"insert into lijstgemeente(id,serienummer,gebruiker,kaart,hostnaam,object,merk,soort,specificatie,vestiging,stats,lokaal,ordernummer,ipadres,aantekening) values({id},'{serienummer}','{gebruiker}','{kaart}','{hostnaam}','{objec}','{merk}','{soort}','{specificatie}','{vestiging}','{status}','{lokaal}','{ordernummer}','{ipadres}','{aantekeningen}')")


#om al de non actieve gebruikers te verwijderen
def verwijder():
    x = getUser()
    for obj in x:
        id = obj.id
        gebruiker = obj.gebruiker
        kaart = obj.kaart
        hostnaam = obj.hostnaam
        serienummer = obj.serienummer
        objec = obj.object
        merk = obj.merk
        soort = obj.soort
        specificatie = obj.specificatie
        vestiging = obj.vestiging
        status = obj.status
        lokaal = obj.lokaal
        ordernummer=obj.ordernummer
        ipadres = obj.ipadres
        aantekening = obj.aantekening
        if status == "Non Actief":
            con.execute(f"DELETE from lijstgemeente where id={id}")




    




'''print("----------------------------------")

q = con.execute("select * from lijstgemeente where object='LAP0250'")
q = con.fetchall()

q = re.sub("'()"," ",str(q))
print(q)'''









