from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

#load the dataset
dataset = loadtxt('pima-indians-diabetes.csv' , delimiter=',')

#split into input and output x and y
x = dataset[:,0:8]
y = dataset[:,8]

#define the model using keras
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#compile the model
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

#fit the model
model.fit(x,y, epochs=150,batch_size=10)

#evalutate the model
_, accuracy = model.evaluate(x, y)
print('Accuracy: %.2f' % (accuracy*100))