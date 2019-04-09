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
        new_username = False
        with open("Credentials.txt", "r") as file:
            for line in file:
                username_create, password_create = line.strip().split(':')
                if username == username_create:
                    found_username = True
                    print("Already exists ")
                    username = input("Please enter a different username")
                    break

        password = input("Please enter a password:")
        ConfirmPassword = input("Please confirm your password:")
        if password == ConfirmPassword:
            with open("Credentials.txt", "a") as file:
                file.write(username + ":" + password)
                file.write("\n")
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
count = 0
if welcome == "y":
    while True:
        while count < 3:
            use = input("Username:")
            pwd = input("Password:")
            found_username = False
            with open("Credentials.txt", "r") as credentials_file:
                for line in credentials_file:
                    username_login, password_login = line.strip().split(':')

                    if use == username_login:
                        found_username = True
                        if pwd == password_login:
                            print("welcome you are now logged in ")
                            break
                        else:
                            print("Password is incorrect!")
                            count += 1
                            if count == 3:
                                print("Attempts exceeded")
                        break
            if not found_username:
                print("Username and or password do not exist!")
                count +=1
                if count == 3:
                    print("Attempts exceeded")
        break



#username = input("Please enter your username: ")
#password = input("Please enter your password: ")
#print("Success")

#create excel database to store username and password
#create login where it will check to make sure the username is not the same as anyone else
#When logging in, look at heart rate file
#if certain heart rate matches username then accept
#if not then deny









