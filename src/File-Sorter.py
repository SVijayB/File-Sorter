import os
import shutil
from modules.extensions import *

if __name__ == "__main__":
    os.system('cls')
    destination = input("\nEnter the address of the folder you want to organise \n> ")
    try:
        os.chdir(destination)
    except:
        print("ERROR : INVALID LOCATION")
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

    print("Sorting Completed...")
