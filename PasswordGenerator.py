
#2h 41m

import time
import subprocess
import sys
import os
from os import path

def access(choice):                                                     # 0 -> prints list of userPasswords, 1 -> changes pin
    if path.exists("savedPin.txt"):
        savedPin = open('savedPin.txt', 'r').read()
        pin = ""
        counter = 3
        while pin != savedPin:
            pin = input("Insert your 4-digit pin to access: ")
            if pin == savedPin:                                         #access granted
                print("You have access")
                time.sleep(1)
                if choice == 0:
                    userPasswords(1)
                elif choice == 1:
                    changePin()
            else:
                counter -= 1
                if counter == 0:
                    print("Sorry the program will close now!")
                    time.sleep(1)
                    sys.exit()
                print("Wrong Pin you have", counter, "guesses left")   #access denied
    else:
        f = open("savedPin.txt", "w")                                  #if savedPin.txt does not exist, creates it
        newPin = input("Please insert a new 4-digit pin: ")             
        f.write(newPin)
        f.close()
        time.sleep(1)

def mainMenu():
    print("Menu")
    print("1. Generate Password")
    print("2. Load saved passwords")
    print("3. Settings")
    print("4. Exit")
    menuInput = int(input())
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
        print("Choose one of the following options: | '1' | '2' | '3' | '4' |")
        print("Please try again.")
        time.sleep(2)
        mainMenu()
    
def generatePassword():
    #to be completed
    return 0

def pinCheck(pin):
    #to be completed
    return 0

def settings():
    print("To change your current pin press 1")
    print("-Maybe a different format for the gened-password- press 2")
    print("To go back to main menu press 3")
    choiceInput = int(input())
    if choiceInput == 1:                                                    #Changes pin
        access(1)
        f = open("savedPin.txt", "r")
        for i in f:
            print("Your new pin is: ", i)
        f.close()
        time.sleep(1)
    elif choiceInput == 2:
        print("-We will see-")
        settings()
    elif choiceInput == 3:
        return None
    else:
        print("Choose one of the following options: | '1' | '2' | '3' |")
        time.sleep(1)
        settings()

def userPasswords(choice):
    try:
        f = open("passwords.txt", "r")
    except IOError:
        f = open("passwords.txt", "w")
        f.close
    if choice == 1:                                                       #Ektypwsi tou arxeiou me ta passwords mono gia choice 1
        for line in f:
            print(line)
        print
    f.close()

def changePin():
    newPin = input("Insert here your new 4-digit pin: ")
    pinfile = open("savedPin.txt", "w+")
    pinfile.write(newPin)    
    pinfile.close()
    

if __name__ == "__main__":
    userPasswords(0)
    print("_______WELCOME TO PASSWORD GENERATOR_______")
    time.sleep(1)
    mainMenu()
