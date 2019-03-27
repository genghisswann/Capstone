########################################
#
# This module is capable of taking a single CSV file and parsing each column into tensors. I think...
#
########################################

import tensorflow as tf
import tensorflow.contrib.eager as tfe
import os

tf.enable_eager_execution()

train_ds_url = "http://download.tensorflow.org/data/iris_training.csv"
train_ds_fp = tf.keras.utils.get_file(fname=os.path.basename(train_ds_url), origin=train_ds_url)
train_ds_lo = 'weightData_test.csv'

col_name = ["Id", "Date", "WeightKg", "WeightLb", "Fat", "BMI", "IsManReport", "LogId"]
feat_name = col_name[:-1]
label_name = col_name[-1]

batch_size = 32

train_ds = tf.contrib.data.make_csv_dataset(
    train_ds_lo,
    batch_size,
    column_names=col_name,
    label_name=label_name,
    num_epochs=1)

features, labels = next(iter(train_ds))

print(features)

dataset = tf.data.Dataset.from_tensor_slices(tf.random_uniform([100, 2]))
print(dataset)

#sess = tf.InteractiveSession()
#print (features.eval())

#with tf.Session as sess:
#   sess.run([features, lables])
