########################################
#
# Module Name: basicReader.py
# Module Purpose: To read in CSV files for futher analysis
#
########################################


import tensorflow as tf
import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler

print(tf.__version__)

tf.enable_eager_execution()

#training_data_df = pd.read_csv("weightData_training.csv")

# determine length of CSV file being read
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
        return i + 1

# file reader
def read_from_csv(filename_queue):
    reader = tf.TextLineReader(skip_header_lines=1)
    _, csv_row = reader.read(filename_queue)
    record_defaults = [[""], [""], [0], [0], [0], [0]]

# Load training data set from CSV file
training_data_df = pd.read_csv("weightData_test.csv")


