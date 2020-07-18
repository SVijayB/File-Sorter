import os
from modules.extensions import *
from modules.colours import *
import time

if __name__ == "__main__":
    os.system('cls')
    logo = open("assets/logo.txt","r")
    output = "".join(logo.readlines())
    grey(output)
    green("\n"+"-"*20)
    version = open("assets/version.txt" , "r").read()
    cyan("File Sorter | " + version)
    time.sleep(1)
    while(True):
        print("\n1) View all extensions.\n2) Add an extension.\n3) Delete an extension.\n4) Exit")
        choice = int(input("What would you like to do?\n> "))
        if(choice == 1):
            pass
        elif(choice == 2):
            pass
        elif(choice == 3):
            pass
        elif(choice == 4):
            green("---- x Thanks for using File Sorter x ----")
            grey("Press any key to exit")
            input()
            break
        else:
            red("ERROR : Invalid choice")