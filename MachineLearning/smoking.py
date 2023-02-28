'''
https://www.kaggle.com/datasets/yusufdede/lung-cancer-dataset
'''

import pandas as pd
from prettytable import PrettyTable
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv('lung_cancer_examples.csv')

df = df.drop(['Name','Surname'],axis=1)
print(df)

#PRint the result as a bar graph
df.Result.value_counts()[0:30].plot(kind='bar')


#visualize data in 16 different plots where its based on the result
sns.set_style("whitegrid")
sns.pairplot(df, hue="Result", size=3)
#plt.show()

sns.lineplot(x=df['Age'],y=df['AreaQ'],data=df)
#plt.show()
sns.lineplot(x=df['Age'],y=df['Alkhol'],data=df)
#plt.show()
sns.lineplot(x=df['Age'],y=df['Smokes'],data=df)
#plt.show()

from sklearn.model_selection import train_test_split

Y = df['Result']
X = df.drop(columns=['Result'])
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.1,random_state=9)

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

lr = LinearRegression()
lr.fit(X_train, Y_train)

predictions = lr.predict(X_test)
Y_test = list(Y_test)
print('=============================')
print(Y_test[1])
print(predictions[1])

pred = []
for i in predictions:
    pred.append(round(i))

print(predictions)
print(Y_test)
print(pred)

print(accuracy_score(Y_test, pred))










