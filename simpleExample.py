########################################
#
# Building a very basic neural network for training
#
########################################

import tensorflow as tf
from tensorflow.python.keras.layers import Input, Dense
import numpy as np

np.random.seed(7)

# loading current dataset
dataset = np.loadtxt("WDTrain.csv", delimiter=",", skiprows=1)
input = dataset[:,1:5]
output = dataset[:,0]

#print(input, output)

# creating model
model = tf.keras.Sequential()
model.add(Dense(12, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compiling model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fitting the model
model.fit(input, output, epochs=1500, batch_size=100)

scores = model.evaluate(input, output)
print ("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

predictions = model.predict(input)
rounded = [round(x[0]) for x in predictions]