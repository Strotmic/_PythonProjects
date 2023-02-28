from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import re
from django.db import connection
import mysql.connector
from lijst.models import *

# Create your views here.

mysql.connector.connect(user='root', password='Gusco10.+789',
                              host='127.0.0.1',
                              database='gemeente')

con = connection.cursor()

#maakt een lijst met alle users uit het excel document
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

def getObj():
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
    return x

#roept de methode op die een lijst returnt met de gebruikers.
def lijst2(request):
    x=getObj()

    return render(request, 'test.html', {'lijst':x})

#roept de methode op die een lijst returnt met de gebruikers.
def it(request):
    x=getObj()
    return render(request,'it.html',{'lijst':x})

#roept de methode op die een lijst returnt met de gebruikers.
def personeel(request):
    x=getObj()
    return render(request,'personeel.html',{'lijst':x})

#deze methode zal de database refreshen, hij dropt deze en maakt dan een nieuwe aan op basis vn het excel document
def refresh(request):
    con.execute("DROP TABLE lijstgemeente")
    con.execute("create table lijstgemeente(id integer primary key not null,serienummer varchar(255) , gebruiker varchar(255), kaart varchar(255), hostnaam varchar(255), object varchar(255), merk varchar(255), soort varchar(255), specificatie varchar(255), vestiging varchar(255), stats varchar(255), lokaal varchar(255), ordernummer varchar(255), ipadres varchar(255),aantekening varchar(1000))")
    update()
    x=getUser()

    return render(request,'test.html',{'lijst':x})
