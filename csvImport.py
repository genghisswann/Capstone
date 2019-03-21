import tensorflow as tf
import os

csv_path = 'weightData_test.csv'
dataset = tf.data.experimental.make_csv_dataset(csv_path, batch_size=32)
iter = dataset.make_one_shot_iterator()
next = iter.get_next()
print(next)
inputs, lables = next['a'], next['b']
#next['Id'], next['Date'], next['WeightKg'], next['WeightPounds'], next['Fat'], next['BMI'], next['IsManualReport'], next['LogId']

#with tf.Session() as sess:
#    sess.run(inputs[i:i+batch_size], labels[i:i+batch_size])
