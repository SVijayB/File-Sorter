import os
import shutil
from modules.extensions import *
from modules.colours import *
import time

if __name__ == "__main__":
    os.system('cls')
    logo = open("../assets/logo.txt","r")
    output = "".join(logo.readlines())
    grey(output)
    green("\n"+"-"*20)
    version = open("../assets/version.txt" , "r").read()
    cyan("File Sorter | " + version)
    time.sleep(1)
    destination = input("\nEnter the address of the folder you want to organise \n> ")
    try:
        os.chdir(destination)
    except:
        red("ERROR : INVALID LOCATION")
    files = os.listdir()

    for current_file in files:
        for ex in extensions:
            for y in range(len(extensions[ex])):
                if (current_file.endswith(extensions[ex][y])):
                    category = str(ex)
                    if not os.path.exists(category):
                        os.makedirs(category)
                    shutil.move(current_file,category)
                    break

    files = filter(os.path.isfile, os.listdir(os.curdir))
    for current_file in files:
        category = "Other"
        if not os.path.exists(category):
            os.makedirs(category)
        shutil.move(current_file,category)
    green("Sorting Completed!")
    grey("Press enter key to exit...")
    input()
