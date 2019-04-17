#Create Account
welcome = input("Do you have an account? y/n: ") #Ask the user if they have an account or not
if welcome == "n": #Creating an account if user does not have account
    while True:
        username = input("Please enter a username:")
        found_username = False
        with open("Credentials.txt", "r") as file: #Open the text file, read 
            for line in file:
                username_create, password_create = line.strip().split(':')
                if username == username_create: #looking to see if the username already exists 
                    found_username = True
                    print("Already exists ")
                    username = input("Please enter a different username")
                    break
            else:
                for line in file: #If username does not exist then move on to password 
                    if not line:
                        break

        password = input("Please enter a password which must be a min 8 characters and a max of 15 characters:")
        ConfirmPassword = input("Please confirm your password: ")
        if len(password) > 15:
            print("password is too long")
        elif len(password) < 8:
            print("password is too short")
        elif len(password) >= 8 and len(password) <= 15:
            with open("Credentials.txt", "a") as file: #write the username and password to the text file 
                file.write(username + ":" + password)
                file.write("\n")
                file.close()
            if password != ConfirmPassword: #make sure passwords match 
                print("Passwords do NOT match!")
            else:
                welcome = input("If you would like to login, press y to login") #if user wants to login 
                welcome = "y"
                break

#Login
def authenticate(use, pwd):
    with open("Credentials.txt", "r") as credentials_file: #open and read the text file 
        for line in credentials_file:
            username_login, password_login = line.strip().split(':')
            if username_login == use and password_login == pwd: #look to see if username and password match whats in text file 
                return True
            elif username_login == use and password_login != pwd: #if username is correct but password is not 
                raise Exception("Password is incorrect!")
            else:
                continue
    raise Exception("Username and/or password do not exist!") #is username and/or password do not match 

if welcome == "y":
    print("\nPlease login")
    is_authenticated = False
    for r in range(3): #user has 3 attempts 
        use = input("Username: ")
        pwd = input("Password: ")

        try: #Exception handling for if there is an incorrect username or password 
            authenticate(use, pwd)
            is_authenticated = True
            break
        except Exception as error:
            print(error)

    if is_authenticated:
        print("Welcome you are logged in")
    else:
        print("Attempts exceeded!")
