import pickle

def functions_main():
    print("1) Add an extension to an already existing category")
    print("2) Add an extension to a new catagory")
    print("3) Delete an extension")
    print("4) View extensions")
    choice = int(input("What would you like to do?\n> "))
        
    pickle_file = open("assets/extensions_data.pkl", 'rb')
    extensions = pickle.load(pickle_file)
    pickle_file.close()
        
    if(choice == 1):
        for ex in extensions:
            print("• " + ex)
        category = input("Which category does the extension belong to? (Type the exact name)\n> ").capitalize()
        new_extension = input("Enter the extension you want to add. Eg: EXE,PNG,JPEG\n> ")
            
        new_extension = ("." + new_extension)
        try:
            extensions[category].append(new_extension)
            pickle_file = open("assets/extensions_data.pkl", 'wb')
            pickle.dump(extensions, pickle_file)
            pickle_file.close()   
            print("Extension has been added")
        except:
            print("ERROR : CATEGORY DOES NOT EXIST")

    elif(choice == 2):
        key = input("Enter the new category to be added\n> ").capitalize() 
        value = input("Enter the extension\n> ")
        value = ("." + value)
        extensions[key] = [value]

        pickle_file = open("assets/extensions_data.pkl", 'wb')
        pickle.dump(extensions, pickle_file)
        pickle_file.close()
            
        print("Extension has been added")

    elif(choice == 3):
        for ex in extensions:
            print("• " + ex)

        category = input("Which category does the extension belong to? (Type the exact name)\n> ").capitalize()
        try:
            for y in range(len(extensions[category])):
                print(extensions[category][y])

            del_extension = input("Enter the extension you want to delete. Eg: EXE,PNG,JPEG\n> ")
            del_extension = ("." + del_extension)
            extensions[category].remove(del_extension)

            pickle_file = open("assets/extensions_data.pkl", 'wb')
            pickle.dump(extensions, pickle_file)
            pickle_file.close()
            print("Extension has been Deleted!")
        except:
            print("ERROR : CATEGORY DOES NOT EXIST")

    elif(choice == 4):
        for ex in extensions:
            print("• " + ex)
        category = input("Which category does the extension belong to? (Type the exact name)\n> ").capitalize()
        try:
            for y in range(len(extensions[category])):
                print("\t->",extensions[category][y])
        except:
            print("ERROR : CATEGORY DOES NOT EXIST")

    else:
        print(choice)
        print("ERROR : INVALID OPTION")


functions_main()

