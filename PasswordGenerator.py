import time
import sys
import random
import os
from os import path

asciiListNumbers = [48,49,50,51,52,53,54,55,56,57]
asciiListCapitals = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
asciiListletters = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
asciiListSpecial = [64,36,33,37]

def access(choice):                                                     # choice: 0 -> prints list of userPasswords, 1 -> changes pin
    if path.exists("savedPin.txt"):
        savedPin = open('savedPin.txt', 'r').read()
        pin = ""
        counter = 3
        while pin != savedPin:
            pin = input("\nInsert your 4-digit pin to access: ")
            if pin == savedPin:                                         #access granted
                print("Access Granted")
                time.sleep(1)
                if choice == 0:
                    userPasswords(1)
                elif choice == 1:
                    changePin()
            else:
                counter -= 1
                if counter == 0:
                    print("\nSorry the program will close now!")
                    time.sleep(1)
                    sys.exit()
                print("\nWrong Pin you have", counter, "guesses left")   #access denied
    else:
        f = open("savedPin.txt", "w")                                  #if savedPin.txt does not exist, creates it
        newPin = input("\nPlease insert a new 4-digit pin: ")             
        f.write(newPin)
        f.close()
        time.sleep(1)
        access(choice)

def mainMenu():
    print("\nMenu")
    print("1. Generate Password")
    print("2. Load saved passwords")
    print("3. Settings")
    print("4. Exit")

    menuInput = input()
    try:
        menuInput = int(menuInput)
    except ValueError:
        print('\nYou did not enter an integer')
        time.sleep(2)
        mainMenu()

    if menuInput<5 and menuInput>0:
        if menuInput == 1:                                          #password generator
            generatePassword()
            mainMenu()
        elif menuInput == 2:                                        #open access
            access(0)
            mainMenu()
        elif menuInput == 3:                                        #open settings
            settings()
            mainMenu()
        elif menuInput == 4:                                        #exit
            sys.exit()        
    else:
        print("\nChoose one of the following options: | '1' | '2' | '3' | '4' |")
        print("Please try again.")
        time.sleep(2)
        mainMenu()

def addToClipBoard(text):
    command = 'echo | set /p nul=' + text + '| clip'
    os.system(command)

def generatePassword():
    tempGen = []
    generated = ""
    
    for i in range(10):
        if i < 2:
            num = random.randint(48,57)
            tempGen.append(chr(num))
        elif i < 5:
            num = random.randint(65,90)
            tempGen.append(chr(num))
        elif i < 8:
            num = random.randint(97,122)
            tempGen.append(chr(num))
        else:
            num = random.randint(0,3)
            num = asciiListSpecial[num]
            tempGen.append(chr(num))
        
    counter = 9
    while counter >= 0:
        num = random.randint(0,counter)
        counter -= 1
        generated += tempGen[num]
        tempGen.remove(tempGen[num])

    addToClipBoard(generated)
    print("Your code is: - " + generated + " -  and is already copied to your clipboard!")
    platform = input("In which platform you will use it? ")
    f = open("passwords.txt", "a")
    f.write(platform + " - " + generated)
    f.close

def pinCheck(pin):                                                          # out: 0 -> Valid, 1 -> Error    
    try:
        if len(pin) == 4:
            pin = int(pin)
        else:
            return 1        
    except ValueError:
        return 1
    return 0

def settings():
    print("\n1. To change your current pin press 1")
    print("2. -Maybe a different format for the gened-password-")
    print("3. Back.")
    choiceInput = int(input())
    if choiceInput == 1:                                                    #Changes pin
        access(1)
        f = open("savedPin.txt", "r")
        for i in f:
            print("\nYour new pin is: ", i)
        f.close()
        time.sleep(1)
    elif choiceInput == 2:
        print("\n-We will see-")
        settings()
    elif choiceInput == 3:
        return None
    else:
        print("\nChoose one of the following options: | '1' | '2' | '3' |")
        time.sleep(1)
        settings()

def userPasswords(choice):
    if path.exists("passwords.txt"):
        f = open("passwords.txt", "r")
        if choice == 1:                                                       #Ektypwsi tou arxeiou me ta passwords mono gia choice 1
            for line in f:
                print(line)
            print
        f.close()
    else:
        f = open("passwords.txt", "w")
        f.close
        pass

def changePin():
    newPin = input("\nInsert here your new 4-digit pin: ")
    out = pinCheck(newPin)
    if out == 0:
        pinfile = open("savedPin.txt", "w")
        pinfile.write(newPin)    
        pinfile.close()
    else:
        print("\nSorry, not valid input!")
        time.sleep(2)
        changePin()    

if __name__ == "__main__":
    userPasswords(0)
    print("_______WELCOME TO PASSWORD GENERATOR_______")
    time.sleep(1)
    mainMenu()
