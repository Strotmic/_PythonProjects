

import requests
from bs4 import BeautifulSoup
import re

page = requests.get('https://www.usingenglish.com/articles/41-ways-to-say-goodbye-in-english.html') # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup

ver = ""
ver2=","
ver3="'"

#x = re.findall("<h1.*>.*</h1>", str(soup))
x = re.findall("<strong.*>.*</strong>", str(soup))
x= re.sub('</span>|<span.*?>', ver, str(x))
x= re.sub("<h3.*?>", ver, str(x))
x= re.sub("</h3>", ver, str(x))
x= re.sub("<strong.*?>", ver, str(x))
x= re.sub("</strong>", ver, str(x))
x= re.sub("[0-9]", ver, str(x))
x= re.sub("[!?]", ver, str(x))
x= re.sub("[.]", ver, str(x))
x = re.sub("'", '"', str(x))
x = re.sub("'", '"', str(x))
x = re.split("[/]",str(x))
x = str(x)
a = x.replace("'", "\"")
#x= re.sub("\s*?,",ver2, str(x) )
#x = re.sub(",,,,",ver2,str(x))
#x = re.sub(",","\n",str(x))
'''x= re.sub()
x= re.sub()
x= re.sub()
x= re.sub()
x = re.sub()'''



print(a)