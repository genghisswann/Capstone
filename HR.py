#import pandas as pd
#import matplotlib.pyplot as plt
#import csv
import xlsxwriter
import openpyxl

#dataset = pd.read_csv("data.csv")
#plt. title("Heart Rate Signal")
#plt.plot(dataset.hart)
#plt.show()

#Create excel sheet
#workbook = xlsxwriter.Workbook('Credentials.xlsx')
#worksheet = workbook.add_worksheet()

#Label the top row
#bold = workbook.add_format({'bold': 1})
#worksheet.write('A1', 'First Name', bold)
#worksheet.write('B1', 'Last Name', bold)
#worksheet.write('C1', 'Username', bold)
#worksheet.write('D1', 'Password', bold)

#To label the top row
#row = 1
#col = 0


#Create Account
welcome = input("Do you have an account? y/n: ")
if welcome == "n":
    while True:
        username = input("Please enter a username:")
        password = input("Please enter a password:")
        ConfirmPassword = input("Please confirm your password:")
        if password == ConfirmPassword:
            file = open("Credentials.txt", "a")
            file.write(username + ":" + password)
            file.close()
            welcome = "y"
            break
        print("Passwords do NOT match!")


#workbook = openpyxl.load_workbook('Credentials.xlsx')
#worksheet = workbook.active

#i = 0
#cell_val = ''

#while cell_val != '':
  #  cell_val = worksheet['E' + i].value
 #   i += 1
#workbook.save('Credentials.xlsx')

#lastName = input("Please enter your last name: ")

#username = input("Please create username")

#password = input("Please create password")

#workbook.close()

#Login
if welcome == "y":
    while True:
        use = input("Username:")
        pwd = input("Password:")
        file = open("Credentials.txt", "r")
        data = file.readline()
        file.close()
        if data == use + ":" + pwd:
            print("Welcome")
            break
        print("Incorrect username or password.")


#username = input("Please enter your username: ")
#password = input("Please enter your password: ")
#print("Success")

#create excel database to store username and password
#create login where it will check to make sure the username is not the same as anyone else
#When logging in, look at heart rate file
#if certain heart rate matches username then accept
#if not then deny









