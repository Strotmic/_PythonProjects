import re
txt = 'Dit is een test'
re.findall('\s',txt)

txt = ('tim.bleuze@gmail.com', "piet2769@hotmail.com", "snowman_420xx@gmail.com", "johan@@hotmail.com", "tim.bleuze@leerling.guldensporenmcollege.")
#re.findall('^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})*$',str(txt))
for i in txt:
    if re.match('^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,6})$',i):
        print(i)