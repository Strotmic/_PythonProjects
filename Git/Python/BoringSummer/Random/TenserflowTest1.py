from gc import callbacks
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from keras.models import Sequential, load_model
from keras.layers import Dense
from datetime import datetime
from packaging import version

import tensorflow as tf
from tensorflow import keras
import tensorboard

df = pd.read_csv('data/Churn.csv')

x = pd.get_dummies(df.drop(['Churn', 'Customer ID'], axis=1))
y= df['Churn'].apply(lambda x: 1 if x=='Yes' else 0)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=.2)

x_train.head()
y_train.head()
print(y)

model = keras.models.Sequential()
model.add(Dense(units=32, activation='relu', input_dim=len(x_train.columns)))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='sgd' , metrics='accuracy')

(train_images, train_labels), _ = keras.datasets.fashion_mnist.load_data()
train_images = train_images / 255.0
logdir="logs/fit/" + datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = keras.callbacks.TensorBoard(log_dir=logdir)

model.fit(x_train, y_train, epochs=10, batch_size=64, callbacks=[tensorboard_callback])

y_hat = model.predict(x_test)
y_hat = [ 0 if val <0.5 else 1 for val in y_hat]

y_hat

print(accuracy_score(y_test, y_hat))
model.save('tfModel1')
