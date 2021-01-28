
#1h 00m

import time
import subprocess
import sys


def entrance():
    try:
        savedPin = open('savedPin.txt', 'r').read()
        pin = ""
        counter = 3
        while pin != savedPin:
            pin = input("Insert your 4-digit pin to access the app: ")
            if pin == savedPin:                                        #access granted
                print("You have access")
            else:
                counter -=1
                if counter == 0:
                    print("Sorry the program will close now!")
                    time.sleep(1)
                    sys.exit()
                print("Wrong Pin you have", counter, "guesses left")   #access denied
    except IOError:
        f = open("savedPin.txt", "w")                                  #if savedPin.txt does not exist, creates it
        newPin = input("Please insert a new 4-digit pin: ")
        f.write(newPin)
        f.close()
        subprocess.check_call(["attrib","+H","savedPin.txt"])          #converts the text file to hidden text file (my only security)

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
        elif menuInput == 2:                                        #open entrance
            entrance()
        elif menuInput == 3:                                        #open settings
            print(2)
        elif menuInput == 4:                                        #exit
            sys.exit()
    else:
        print("Sorry wrong input! Please try again.")
        time.sleep(1)
        mainMenu()
    
def generatePassword():
    

    

if __name__ == "__main__":
    print("_______WELCOME TO PASSWORD GENERATOR_______")
    time.sleep(1)
    mainMenu()
