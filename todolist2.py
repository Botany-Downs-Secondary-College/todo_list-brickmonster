#Eason Xuan
#Feb, 2021

# Imports the system module, which allows the program to quit
import sys
# The to do list
to_do = []

# Asks the user what they want to do
def menu():
    while True:
        print("Choose from the following in the menu by pressing 1, 2, or 3. \n"
              "1. Add a task \n"
              "2. View List \n"
              "3. Exit")
        try:
            user_input = int(input(""))
            if user_input == 1:
                to_do_list()
            elif user_input == 2:
                list()
            elif user_input == 3:
                print("Thank you and goodbye, here is your list:")
                print("\n - ".join(to_do))
                sys.exit()
        except ValueError:
            print('Only enter in a number 1, 2 or 3.')
       
# The loop to add stuff to the to do list
def to_do_list():
    while True:
        print("Enter what you want to add to the to do list. If done type exit")
        add_list = input(' ')
        if add_list == 'exit':
            menu()
        else:
            to_do.append(add_list)
               
# It will print the to do list
def list():
    print("Here is your to do list:")
    print("\n - ".join(to_do))
   
# Calls the menu
menu()