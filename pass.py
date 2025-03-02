import string
import random
file = open("test.txt", "w")
file.write("Passwords Stored in a file: " + "\n")
file.close()
listUser = []
lowerc = []
lowerc = list(string.ascii_lowercase)

upperc = []
upperc = list(string.ascii_uppercase)

numbers = []
numbers = list(string.digits)

characters = []
characters = list(string.punctuation)

passwords = []

def genLower():
    ran = random.randint(0,len(lowerc)-1)
    return lowerc[ran]

def genUpper():
    ran = random.randint(0,len(upperc)-1)
    return upperc[ran]

def genNum():
    ran = random.randint(0,len(numbers)-1)
    return numbers[ran]

def genChar():
    ran = random.randint(0,len(characters)-1)
    return characters[ran]


def addVal():
    ranList = random.randint(0,3)
    match (ranList):
        case 0:
            val = genLower()
        case 1:
            val = genUpper()
        case 2:
            val = genNum()
        case 3:
            val = genChar()
    return val

def textAppend(password):
     file = open("test.txt", "a")
     file.write(password + "\n")

def generatePass():
    password = ""
    for x in range(0,12, 1):
        password = password + addVal()
    print("Your password is: " + password)
    passwords.append(password)
    textAppend(password)

def listoutput():
     print("Passwords stored in a list: ")
     for x in range(len(passwords)):
          print(passwords[x])   
     print("")

def fileoutput():
     f = open('test.txt', 'r')
     for line in f:
          print(line)
     f.close()

def login():
    return True

def signup():
    loop = True
    while loop:
        username = str(input("Enter a username: "))
        for user in listUser:
            if username == user:
                print("Username has already been registered")
                continue
            else:
                listUser.append(username)
                confirmUser = username
                loop = False
                break
    return confirmUser

def accountMenu():
    username = ""
    count = True
    while count == True:
        account = str(input("Do you want to use an account? (y/n)"))
        if account.lower() == "y":
            userMenu()
        elif account.lower() == "n":
            count = False
        else: 
            print("Try again")
    return username

def userMenu():
    count = 0
    while count <1:
        userType = bool(input("Do you want to login? If so type True"))
        match (userType):
            case True:
                login()
            case False:
                signup()
            case _:
                print("Invalid option")

def passMenu():
    count = True
    while count == True:
        try:
            choice=int(input("Type 1 to generate a password, or 2 to quit, 3 to view current passwords generated: "))
            if choice == 1:
                generatePass()
            elif choice == 2:
                print("Goodbye")
                break
            elif choice == 3:
                listoutput()
                fileoutput()
            else: 
                print("Please enter a valid option")
                continue
        except ValueError:
            print("Integer Required")

def main():
    print("Hi! Welcome to my strong password generator! This generates passwords randomised using characters, letters and numbers...")
    print("Each password is 12 characters long to ensure it is secure.")
    accountMenu()
    passMenu()



main()
