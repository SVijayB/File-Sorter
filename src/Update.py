import os
from modules.functions import *
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
    while(True):
        functions_main()
        green("\n"+"-"*20)