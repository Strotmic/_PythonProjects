
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

#Read in the csv file
df = (pd.read_csv('COVID-19 Cases.csv'))
df = df['Cases']

#Label the columns
df = pd.DataFrame(pd.read_csv('COVID-19 Cases.csv'), columns=['Case_Type','Cases','Difference','Date','Country_Region','Province_State','Admin2','Combined_Key','FIPS','Lat','Long','Location','Table_Names','Prep_Flow_Runtime'])

#Empty dictionary 
countrys = {}

#For lus where we go trought the countrys and count together all the cases for the same countrys
for i in range(len(df)):
    if df['Cases'][i]>0:

        if df['Country_Region'][i] in countrys.keys():
            #will change the value of the key by adding the amount of cases
            countrys[df['Country_Region'][i]] += df['Cases'][i].item()
        else:
            #adds a new key value pair where the key is the country and the value is the amount of cases
            countrys[df['Country_Region'][i]] = df['Cases'][i].item()

        #print(f"{df['Cases'][i]} in {df['Country_Region'][i]} date: {df['Date'][i]}")

#Set up the table with the titles and left align
x = PrettyTable()
x.field_names = ['Country', 'Cases']
x.align['Country'] = 'l'
x.align['Cases'] = 'l'

#sort the dictionary on the values
countrys = {key: value for key, value in sorted(countrys.items(), key=lambda item:item[1])}

#add the rows to the table and get a total numbers of cases
keys = list(countrys.keys())
values = list(countrys.values())
total = 0
for i in range(len(countrys)):
    total += countrys[keys[i]]
    x.add_row([keys[i],countrys[keys[i]]])
    
#sorts the table from largest to smallest cases
x.sortby = "Cases"
x.reversesort = True
print(x)
print(f'Totaal aantal cases = {total}')

#Make a barplot with only the 8 last countrys (The 8 biggest)
ax = sns.barplot(keys[-8:], values[-8:])

#add the labels to the top of the bars (with fontsize 8 and fmt='%d' so it doesnt say 1e6)
for i in ax.containers:
    ax.bar_label(i,fmt='%d', fontsize='8')

#set the labels and the title for the graph
ax.set(xlabel = 'Countrys', ylabel= 'Cases')
ax.set(title='Every country with more than 1 million cases')

#change the y axis to non scientific numbers (without the 1e6)
plt.ticklabel_format(style='plain', axis='y')

#set a lim for the y axis and then show the plot
plt.ylim(0,7000000)
plt.show() 















