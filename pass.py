import string
import random
file = open("test.txt", "w")
file.write("Passwords Stored in a file: " + "\n")
file.close()
listUser = []
listUser.append("ubshx")
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

def textAppend(password, username):
     file = open("test.txt", "a")
     file.write(username + ": " + password + "\n")

def generatePass(username):
    password = ""
    for x in range(0,12, 1):
        password = password + addVal()
    print("Your password is: " + password)
    passwords.append(password)
    textAppend(password, username)

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
    loop = True
    condition = True
    count = 0
    countLeft = 2
    while loop:
        username = str(input("Enter a username: "))
        for user in listUser:
            if username == user:
                condition = False
        if condition == False:
            confirmUser = username
            break
        elif condition == True and count==3:
            print("Signing up...")
            confirmUser = signup()
            loop = False
        else: 
            print(f"Username is invalid, {countLeft} more tries")
            countLeft-=1
            count+=1
        
    return confirmUser

def signup():
    loop = True
    condition = True
    while loop:
        username = str(input("Enter a username: "))
        for user in listUser:
            if username == user:
                print("Username has already been registered")
                condition = False
        if condition == False:
            continue
        else: 
            confirmUser = username
            loop = False 
    return confirmUser

def accountMenu():
    username = "Default user"
    count = True
    while count == True:
        account = str(input("Do you want to use an account? (y/n)"))
        if account.lower() == "y":
            username = userMenu()
            count = False
        elif account.lower() == "n":
            count = False
        else: 
            print("Try again")
    return username

def userMenu():
    username = ""
    count = 0
    while count <1:
        userType = str(input("Do you want to login? If so type True, or False for signup: "))
        match (userType):
            case "True":
                print("Logging in...")
                username = login()
                count+=1
            case "False":
                print("Signing up...")
                username = signup()
                count+=1
            case _:
                print("Invalid")
    return username

def passMenu(username):
    count = True
    while count == True:
        try:
            choice=int(input("Type 1 to generate a password, or 2 to quit, 3 to view current passwords generated: "))
            if choice == 1:
                generatePass(username)
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
    username = accountMenu()
    passMenu(username)



main()
