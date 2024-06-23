import string
import random
file = open("test.txt", "w")
file.write("Passwords Stored in a file: " + "\n")
file.close()

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
    for x in range(0,12):
        password = password + addVal()
    print("Your password is: " + password)
    passwords.append(password)
    textAppend(password)

def listoutput():
     print("Passwords stored in a list: ")
     for x in range(0,len(passwords)):
          print(passwords[x])   
     print("")

def fileoutput():
     f = open('test.txt', 'r')
     for line in f:
          print(line)
     f.close()

def main():
    choice = int
    count = True
    print("Hi! Welcome to my strong password generator! This generates passwords randomised using characters, letters and numbers")
    print("Each password is 12 characters long to ensure it is secure.")
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

main()
