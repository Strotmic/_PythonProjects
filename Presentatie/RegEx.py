import re

txt = "The rain in spain"
replace = "x"

x=re.sub("[a-m]", replace, txt)
print(x)
print("-------------------------------")

x=re.sub("[a-m]", replace, txt,1)
print(x)
print("-------------------------------")

txt = "The rain in Spain. This is a test! This also? End" 
x = re.split("[.]|[?]|[!]",  txt)
print(x)
print("-------------------------------")

txt="The rain in spain"
x=re.sub(".", replace,txt)
print(x)
print("-------------------------------")

x=re.sub("a.", replace,txt)
print(x)
print("-------------------------------")

txt = ('seven', 'even','prevent', 'revenge', 'maven', 
    'eleven', 'amen', 'event')
for i in txt:
    if re.match('^e.+',i):
        print(i)
print("-------------------------------")

for i in txt:
    if re.match('.+n$',i):
        print(i)
print("-------------------------------")

txt = "The rain in Spain." 
x = re.findall('Sp.?n',  txt)
print(x)
print("-------------------------------")

x = re.findall('S.+in',  txt)
print(x)
print("-------------------------------")

x = re.findall('S.*in',  txt)
print(x)
print("-------------------------------")

x = re.findall("Sp.{2}n",  txt)
print(x)
print("-------------------------------")

x = re.findall("Spain|rain",  txt)
print(x)
print("-------------------------------")

x = re.findall("T(he)",  txt)
print(x)
print("-------------------------------")

txt = ('tim.bleuze@gmail.com', "piet2769@hotmail.com", "snowman_420xx@gmail.com", "johan@@hotmail.com", "tim.bleuze@leerling.guldensporenmcollege.")
#re.findall('^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})*$',str(txt))
for i in txt:
    if re.match('^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,6})$',i):
        print(i)
