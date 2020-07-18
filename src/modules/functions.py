import pickle

def writing():
    pickle_file = open("assets/extensions_data.pkl", 'wb')
    pickle.dump(extensions, pickle_file)
    pickle_file.close()

def reading():
    pickle_file = open("assets/extensions_data.pkl", 'rb')
    extensions = pickle.load(pickle_file)
    pickle_file.close()
    print(extensions)

def updating():
    while(True):
        print("1) Add an extension to an already existing category")
        print("2) Add an extension to a new catagory")
        print("3) Delete an extension")
        choice = int(input("What would you like to do?\n> "))
        
        pickle_file = open("assets/extensions_data.pkl", 'rb')
        extensions = pickle.load(pickle_file)
        pickle_file.close()
        
        if(choice == 1):
            i = 1
            for ex in extensions:
                print(i,"\b) " + ex)
                i = i+1
            category = input("Which category does the extension belong to?(Type the exact name)\n> ").capitalize()
            new_extension = input("Enter the extension you want to add. Eg: EXE,PNG,JPEG\n> ")
            
            new_extension = ("." + new_extension)
            extensions[category].append(new_extension)

            pickle_file = open("assets/extensions_data.pkl", 'wb')
            pickle.dump(extensions, pickle_file)
            pickle_file.close()
            
            print("Extension has been added")
            break

        elif(choice == 2):
            key = input("Enter the new category to be added\n> ").capitalize() 
            value = input("Enter the extension\n> ")
            value = ("." + value)
            extensions[key] = [value]

            print(extensions)

            pickle_file = open("assets/extensions_data.pkl", 'wb')
            pickle.dump(extensions, pickle_file)
            pickle_file.close()
            
            print("Extension has been added")
            break

        elif(choice == 3):
            i = 1
            for ex in extensions:
                print(i,"\b) " + ex)
                i = i+1
            category = input("Which category does the extension belong to?(Type the exact name)\n> ").capitalize()
            i = 1
            for y in range(len(extensions[category])):
                print(extensions[category][y])
            del_extension = input("Enter the extension you want to delete. Eg: EXE,PNG,JPEG\n> ")
            del_extension = ("." + del_extension)
            extensions[category].remove(del_extension)

            pickle_file = open("assets/extensions_data.pkl", 'wb')
            pickle.dump(extensions, pickle_file)
            pickle_file.close()
            
            print("Extension has been Deleted!")
            break

        else:
            print(choice)
            print("ERROR : INVALID OPTION")
            break