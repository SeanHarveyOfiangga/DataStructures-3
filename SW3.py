# Write a python program for contact tracing:

# - Display a menu of options
# 	Menu:
# 		 1 -> Add an item
# 		 2 -> Search
# 		 3 -> Exit (y/n)
# - Allow user to select item in the menu (check if valid)
# - Perform the selected option
# 		- Option 1: Ask personal data for contact tracing (Listed are sample only, add more)
# 				   Use dictionary to store the info
# 				   Use the full name as key
# 				   The value is another dictionary of personal information
# 		- Option 2: Search, ask full name then display the record
# 		- Option 3: Ask the user if want to exit or retry.

# Note: 
# - Your program should be uploaded to github before 4pm
# - Record a demo presenting your program
# - Send the demo or link of demo directly to my messenger

# Example Output:

# Menu:
#  1 -> Add an item
#  2 -> Search
#  3 -> Exit (y/n)

# What do you want to do? (1-3): 1
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890
# Saved!
# What do you want to do? (1-3): 2
# Full name: Danilo Madrigalejos
# Age: 30
# Address: Eastwood
# Phone number: 1234567890 What do you want to do? (1-3): 3
# Exit? n

# Sean Harvey S. Ofiangga BSCOE 2-6
# Seatwork 3



#intro
def intro():
    print("\033[01m\033[30m\033[47mWelcome to Contact Tracing Program!\033[0m")
intro()


# Codes for the commands
allcontactinfo = {}
def main():
    # Menu
    print("""\n\033[01m========= MENU =========\033[0m
    \033[31m\033[01m1 -> Add an item\033[0m
    \033[32m\033[01m2 -> Search\033[0m
    \033[33m\033[01m3 -> Exit \033[0m
\033[01m========================\033[0m""")                              
    while True:
        # User choice on menu
        user = int(input("\n\033[36mWhat do you want to do?: \033[0m"))
        # Option 1
        if user == 1:
            print("\n\033[01m**********************************************************\033[0m")
            username = input("           \033[35mPlease pick a unique username: \033[0m")
            global info
            name = input("\nEnter your \033[01m\033[31mname: \033[0m")
            age = input("Enter your \033[01m\033[32mage: \033[0m")
            address = input("Enter your \033[01m\033[33maddress: \033[0m")
            contact = input("Enter your contact \033[01m\033[34mnumber: \033[0m")
            info =f"""\n\033[01m\033[31mName \033[0m:\033[0m {name}\033[0m
\033[01m\033[32mAge \033[0m:\033[0m {age}\033[0m
\033[01m\033[33mAddress \033[0m:\033[0m {address}\033[0m
\033[01m\033[34mContact Number \033[0m:\033[0m {contact}\033[0m"""
            newcontactinfo = {
                (f"{username}") : info 
            }
            allcontactinfo.update(newcontactinfo)
            print(f"\n\033[01m\033[30m\033[42m========= The username '{username}' has been added successfully! =========\033[0m")
            main()
        # Option 2    
        elif user == 2:
            find = input("\n\033[35mPlease enter your username: \033[0m")
            for key in allcontactinfo:
                if key == find:    
                    print(f"\n\033[01m\033[43m\033[30m========= Here are all the informations under the username '{find}': =========\033[0m")
                    print(allcontactinfo.get(find))
                    print("\n==============================================================================")
                    main()
            else:
                print(f"\n\033[01m\033[43m\033[30m========= There is no '{find}' in our system =========\033[0m")
                main()
        # Option 3
        elif user == 3:
            while True:
                ext = input("\n\033[47mAre you sure that you want to exit? \033[0m(\033[32my\033[0m/\033[31mn\033[0m): ").lower()
                if ext == "y":
                    print("\n\033[01m\033[30m\033[47mThank you for using the Contact Tracing Program, bye! :)\033[0m")
                    exit()
                elif ext == "n":
                    main()
                else:
                    continue
        else:
            continue                   
main()
        


