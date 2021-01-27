import time
import subprocess
import os


def entrance():
    print("_______WELCOME TO PASSWORD GENERATOR_______")
    time.sleep(1)
    

    if os.stat("savedPin.txt").st_size == 0:
        f = open("savedPin.txt", "w")
        newPin = input("Please type your new 4-digit pin: ")
        f.write(newPin)
        f.close()
        subprocess.check_call(["attrib","+H","savedPin.txt"])
    else:
        savedPin = open('savedPin.txt', 'r').read()
        pin = input("Insert your pin to access the app: ")
        if pin == savedPin:
            print("You have access")
        else:
            print("Wrong")


if __name__ == "__main__":
    entrance()