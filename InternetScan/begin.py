from bs4 import BeautifulSoup
import requests
import webbrowser as wb
def test():
    from googlesearch import search
    
    zoekterm=input('Wat wilt u zoeken? ')
    hoeveel=input('Hoeveel resultaten wilt u? ')
    html=input('Wilt u de html code hebben indien dit mogelijk is ja/nee: ')
    wb.open_new_tab('www.google.com')
    lijst=[]
    for i in search(zoekterm, tld='co.in',stop=int(hoeveel)):
        print(f'{i}\n')
        lijst.append(i)
        page = requests.get(f'{i}') # Getting page HTML through request
        if html=='ja':
            soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup
            soup = str(soup)
            print(soup)
            print('------------------------------------------------------------------------------------------------------------')
        search = i
        wb.open_new_tab(search)
        continue
    print(f'De geopende websites zijn {lijst}')
    k=input("type ok to close ") 
    if k!='':
        print('sluiten')

test() 