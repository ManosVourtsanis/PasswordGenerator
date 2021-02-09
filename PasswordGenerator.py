
#4h 11m

import time
import subprocess
import sys
import os
from os import path

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
    
def generatePassword():
    #to be completed
    return 0

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
