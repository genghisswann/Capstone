#Create Account
welcome = input("Do you have an account? y/n: ")
if welcome == "n":
    while True:
        username = input("Please enter a username:")
        found_username = False
        with open("Credentials.txt", "r") as file:
            for line in file:
                username_create, password_create = line.strip().split(':')
                if username == username_create:
                    found_username = True
                    print("Already exists ")
                    username = input("Please enter a different username")
                    break
            else:
                for line in file:
                    if not line:
                        break

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
            if password != ConfirmPassword:
                print("Passwords do NOT match!")
            else:
                welcome = input("If you would like to login, press y to login")
                welcome = "y"
                break

#Login
def authenticate(use, pwd):
    with open("Credentials.txt", "r") as credentials_file:
        for line in credentials_file:
            username_login, password_login = line.strip().split(':')
            if username_login == use and password_login == pwd:
                return True
            elif username_login == use and password_login != pwd:
                raise Exception("Password is incorrect!")
            else:
                continue
    raise Exception("Username and/or password do not exist!")

if welcome == "y":
    print("\nPlease login")
    is_authenticated = False
    for r in range(3):
        use = input("Username: ")
        pwd = input("Password: ")

        try:
            authenticate(use, pwd)
            is_authenticated = True
            break
        except Exception as error:
            print(error)

    if is_authenticated:
        print("Welcome you are logged in")
    else:
        print("Attempts exceeded!")
