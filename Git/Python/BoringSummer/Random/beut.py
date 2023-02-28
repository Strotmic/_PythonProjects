import requests
from bs4 import BeautifulSoup


site = requests.get("https://www.upbit.com/service_center/notice")
soup = BeautifulSoup(site.content , 'lxml' )
r = soup.find("div", attrs={"class":"tableB"})
 