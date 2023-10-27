import os
import time
from colorama import Fore, Style

try:
    green = Fore.GREEN
    red = Fore.RED
    reset = Style.RESET_ALL

    print("This is your current directory:",os.getcwd())

    print("---------------------------------------------------------------------------------------------------")


    directory = os.listdir(path='.')

    Running = True

    while Running:
        print("Press 1 to see the following directories:")
        print("Press 2 to change directories:")
        print("Press 3 to quit at any time")

        print("---------------------------------------------------------------------------------------------------")

        choice = input("Choose one of the options:")

        if choice == "1":
            print("Here are your directories!")
            time.sleep(3)
            print(directory)
            print("---------------------------------------------------------------------------------------------------")


        elif choice == "2":
            
            choose_dir = input("Choose what directory you wanna switch to:")
    
            if choose_dir in directory:
                
                os.chdir(choose_dir)
                time.sleep(0.75)
                print(f"{green}Success! {reset}This is your updated directory:",os.getcwd())
                print("---------------------------------------------------------------------------------------------------")

            elif choose_dir not in directory:
                print(f"{red}What your are searching has not been found. Please double check what you typed!{reset}")
                print("---------------------------------------------------------------------------------------------------")

        elif choice == "3":
            Running = False
            time.sleep(1)
            print("Bye!!!")
            break

    else:
        print(f"{red}Invalid choice{reset}")
        print("---------------------------------------------------------------------------------------------------")

except NotADirectoryError:
    print(f"{red}Bro this aint a directory dummy!!!!{reset}")

    
