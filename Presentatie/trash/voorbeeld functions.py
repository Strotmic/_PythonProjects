import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.search("\s", txt)
print(x)

txt = "The rain in Spain"
print(re.search("Spain", txt))

txt = "The rain in Spain"
print(re.search("\D", txt))

txt = "The rain in Spain"
print(re.search("\d", txt))

txt = "The rain 2 in Spain"
print(re.search("\d", txt))

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

txt = "The rain in Spain"
x = re.split("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.split("ai", txt,1)
print(x)

replace = "  ik ben aangepast  "
txt = "The rain in Spain"
x = re.sub("ai",replace, txt)
print(x)
replace = "oi"
txt = "The rain in Spain"
x = re.sub("ai",replace, txt,1)
print(x)

txt = "The rain in Spain. Where ever it goes. The snow will even hit Madrid" 
x = re.findall("Sp.{2}n",  txt)
print(x)

replace = "oi"
txt = "The rain in Spain."
x = re.findall('^T.*e$', txt)
print(x)












