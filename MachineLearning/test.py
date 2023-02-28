'''Repository for the daily counts of coronavirus, including confirmed, deaths, and recovered, provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE). Data cleaned and organized to make the it easier to visualize and analyze by Tableau Inc.

​About

* Refreshed daily by 9:00am EST
* See the Data dictionary for a description of the column names
* The updates thread will be used to summarize updates to the dataset

Sources

* Johns Hopkins's repo on GitHub: https://github.com/CSSEGISandData/COVID-19
* COVID-19 Data Hub: https://www.tableau.com/covid-19-coronavirus-data-resources
* COVID-19 Data Hub FAQ: https://www.tableau.com/about/blog/2020/3/coronavirus-data-hub-faq'''


import pandas as pd
from prettytable import PrettyTable
import seaborn as sns
import matplotlib.pyplot as plt



df = (pd.read_csv('COVID-19 Cases.csv'))
df = df['Cases']




df = pd.DataFrame(pd.read_csv('COVID-19 Cases.csv'), columns=['Case_Type','Cases','Difference','Date','Country_Region','Province_State','Admin2','Combined_Key','FIPS','Lat','Long','Location','Table_Names','Prep_Flow_Runtime'])


countrys = {}

for i in range(len(df)):
    if df['Cases'][i]>0:

        if df['Country_Region'][i] in countrys.keys():
            countrys[df['Country_Region'][i]] += df['Cases'][i].item()
        else:
            countrys[df['Country_Region'][i]] = df['Cases'][i].item()

        #print(f"{df['Cases'][i]} in {df['Country_Region'][i]} date: {df['Date'][i]}")

x = PrettyTable()
x.field_names = ['Country', 'Cases']
x.align['Country'] = 'l'
x.align['Cases'] = 'l'

countrys = {key: value for key, value in sorted(countrys.items(), key=lambda item:item[1])}

keys = list(countrys.keys())
values = list(countrys.values())
total = 0
for i in range(len(countrys)):
    total += countrys[keys[i]]
    x.add_row([keys[i],countrys[keys[i]]])
    
x.sortby = "Cases"
x.reversesort = True
print(x)
print(f'Totaal aantal cases = {total}')


ax = sns.stripplot(keys[-8:], values[-8:])

ax.set(xlabel = 'Countrys', ylabel= 'Cases')

plt.ylim(0,7000000)
plt.show()
print('done')















