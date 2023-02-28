x = {
    "merk": "BMW",
    "model": "M3 Sedan",
    "naam": "diellon"
}

x['bouwjaar'] = '2012'


x.update({'model': 'F30 Ici', 'bouwjaar': "2017"})


x.pop('naam')

print(x)


y = {
    "merk": "Mercedes",
    "model": "CG",
    "naam": "Tim"
}

z = {
    "merk": "Audi",
    "model": "rs",
    "naam": "adnres"
}

garage = {"auto1": x, "auto2": y, "auto3": z}

for key, value in garage.items():
    print(key, value)
