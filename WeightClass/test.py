import re
s =' een twee'
dic = {"een":1,"twee":2,"drie":3}
key_list = list(dic.keys())
val_list = list(dic.values())
s=re.sub("\s","/",s )
for key in dic.keys():
    
    if f"{key}" in s:
        s= re.sub(f"{key}",f"{dic.get(key) }",s)

print(s)
    
   
   
   