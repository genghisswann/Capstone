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

################################### CODE START ###################################

#RETURNS A BOOL VALUE TO SIGNIFY IF USER IS CURRENTLY LOGGED IN OR NOT
def loginFunc():
    welcome = input("Do you have an account? y/n: ")

#YES CHOICE
    if welcome == "y" or welcome == "Y" or welcome == "yes" or welcome == "Yes" or welcome == "YES":
        print ("Ya")

        while True:
            count = 0
            while count < 3:
                print("\nPlease login ")
                use = input("Username: ")
                pwd = input("Password: ")
                found_username = False
                with open("Credentials.txt", "r") as credentials_file:
                    for line in credentials_file:
                        username_login, password_login = line.strip().split(':')

                        if use == username_login:
                            found_username = True
                            if pwd == password_login:
                                print("\nWelcome you are now logged in ")
                                return True
                            else:
                                print("\nPassword is incorrect!")
                                count += 1
                                if count == 3:
                                    print("\nAttempts exceeded")
                            return False


                    if not found_username:
                        print("\nUsername and or password do not exist!")
                        count += 1
                        if count == 3:
                            print("Attempts exceeded")
                    else:
                        return False
            break




#NO CHOICE
    elif welcome == "n" or welcome == "N" or welcome == "no" or welcome == "No" or welcome == "NO":
        print ("Na")

        while True:
            username = input("Please enter a username:")
            new_username = False
            with open("Credentials.txt", "w+") as file:
                for line in file:
                    username_create, password_create = line.strip().split(':')
                    if username == username_create:
                        found_username = True
                        print("Already exists ")
                        username = input("Please enter a different username")
                        return False

            password = input("Please enter a password which must be a min 8 characters and a max of 15 characters:")
            ConfirmPassword = input("Please confirm your password: ")
            if len(password) > 15:
                print("password is too long")
            elif len(password) < 8:
                print("password is too short")
            elif len(password) >= 8 and len(password) <= 15:
                with open("Credentials.txt", "a") as file:
                    file.write(username + ":" + password)
                    file.write("\n")
                    file.close()
                    return False
            if password != ConfirmPassword:
                print("Passwords do NOT match!")

#EXIT OPTION (DEBUGGING)
    elif welcome == "exit":
        print("Exiting...")
        exit()

#INVALID CHOICE
    else:
        print ("Invalid Input")
        return False




# Driver program
if __name__ == "__main__":
    isLogged = False
    while isLogged == False:
        print ("Please Login")
        print("Login Status: ", isLogged, "\n\n")
        isLogged = loginFunc()

    print ("Login function done")

