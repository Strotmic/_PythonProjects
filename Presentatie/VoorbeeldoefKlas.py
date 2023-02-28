import requests
from bs4 import BeautifulSoup
import re

page = requests.get('https://www.standaard.be/') # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup

print(soup)
ver = ""
ver2=","

#x = re.findall("<h1.*>.*</h1>", str(soup))
x = re.findall("<h1.*>.*\n(.*)\n(.*)\n(.*)\n?(.*)</h1>", str(soup))
x= re.sub('</span>|<span.*?>', ver, str(x))
x= re.sub("'", ver, str(x))
x= re.sub("[()]", ver, str(x))
x= re.sub("\s*?,",ver2, str(x) )
x = re.sub(",,,,",ver2,str(x))
x = re.sub(",","\n",str(x))
'''x= re.sub()
x= re.sub()
x= re.sub()
x= re.sub()
x = re.sub()'''



print(x)

