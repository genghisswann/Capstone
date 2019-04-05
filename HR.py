#import pandas as pd
#import matplotlib.pyplot as plt
#import csv
import xlsxwriter
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

#dataset = pd.read_csv("data.csv")
#plt. title("Heart Rate Signal")
#plt.plot(dataset.hart)
#plt.show()

#Create excel sheet
workbook = xlsxwriter.Workbook('Credentials.xlsx')
worksheet = workbook.add_worksheet()

#Label the top row
bold = workbook.add_format({'bold': 1})
worksheet.write('A1', 'First Name', bold)
worksheet.write('B1', 'Last Name', bold)
worksheet.write('C1', 'Username', bold)
worksheet.write('D1', 'Password', bold)

#To label the top row
row = 1
col = 0

df = pd.read_excel('Credentials.xlsx', sheetname = 'Sheet1')
print("Column headings:")
print(df.columns)

#Create Account
firstName = input("Please enter your first name: ")

#lastName = input("Please enter your last name: ")

#username = input("Please create username")

#password = input("Please create password")

workbook.close()

#Login
#username = input("Please enter your username: ")
#password = input("Please enter your password: ")
#print("Success")












#with open('data.csv') as csvDataFile:
 #   csvReader = list(csv.reader(csvDataFile))
  #  df.sort_values([col1, col2])
   # for row in csvReader:
    #  print(df.sort_values)




#create excel database to store username and password
#create login where it will check to make sure the username is not the same as anyone else
#When logging in, look at heart rate file
#if certain heart rate matches username then accept
#if not then deny






