# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all my messages")
    print("5. Block friend")
    print("6. Send a message")
    print("7. <- Go back ")
    return input("Please Choose a number: ")

def editdetails():
    print("")
    print("1. Change name")
    print("2. Chnage age")
    print("3. Change email")
    print("4. <- Go back ")
    return input("Please Choose a number: ")


