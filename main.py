from dictionary import dict_wrapper
from file_management import file_management
import os

#menu screen
def print_menu():
    print("------------------------------------------|")
    print("(1) - Create an empty phone book          |")
    print("(2) - Add entry to phone book             |")
    print("(3) - Get entry from phone book           |")
    print("(4) - list entries from phonebook         |")
    print("(5) - delete entry from phone book        |")
    print("(6) - clear all entries from phone book   |")
    print("                                          |")
    print("(7) - save phone book                     |")
    print("(8) - load phone book                     |")
    print("(9) - delete phonebook                    |")  
    print("(10) - list saved phone books             |")
    print("                                          |")
    print("(11) - backup phonebooks to server        |")
    print("(12) - restore phonebooks from server     |")
    print("(q) - quit                                |")
    print("------------------------------------------|")

#get user input and interpret and execute the correct action depending on input from the user
def interpret_input():

    quit = 0    #to determine whether to exit the program
    phonebook = dict_wrapper()  #phonebook instance
    file_m = file_management() #file_management instance

    #main loop
    while quit !=1:

        user_input = input("<prompt('0'-clear)>:")  #main prompt to obtain user input

        #clear/refresh the screen
        if user_input=='0':
            os.system('clear')
            print_menu()

        #create fresh phonebook dictionary
        if user_input=='1':
            print("*phone book created*")
            phonebook = dict_wrapper()

        #add entry
        elif user_input=='2':
            key = input("Enter fullname of contact:")
            value = input("Enter contact's number:")
            phonebook.setEntry(key,value)
            print("*entry added*")

        #get entry
        elif user_input=='3':
            key = input("Enter contact:")
            phonebook.getEntry(key)

        #list entries
        elif user_input=='4':
            phonebook.listEntries()

        #delete entry
        elif user_input=='5':
            key = input("Enter contact to delete:")
            phonebook.deleteEntry(key)

        #clear all entries
        elif user_input=='6':
            phonebook.deleteAllEntries()

        #save phonebook to hdd
        elif user_input=='7':
            u_input = input("save phonebook as:")
            file_m.saveToFile(u_input,phonebook.getDictionary())

        #load phonebook from hdd
        elif user_input=='8':
            u_input = input("Enter phonebook to load(do not include '.json'):")
            phonebook.setDictionary(file_m.loadFromFile(u_input))

        
        #delete phonebook from hdd
        elif user_input=='9':
            u_input=input("Enter phonebook to delete(do not include '.json'):")
            file_m.deleteFile(u_input)

        #list phonebooks
        elif user_input=='10':
            file_m.viewFiles()

        
        #backup files to server
        elif user_input=='11':
            file_m.backup_files()

        #restore file from server
        elif user_input=='12':
            file_m.restore_files()

        #quit
        elif user_input=='q':
            quit=1


#main function
def main():
    print_menu()
    interpret_input()

main()      #main program



