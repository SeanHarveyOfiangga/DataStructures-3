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
    print("Welcome to Contact Tracing Program!")
intro()


# Codes for the commands
allcontactinfo = {}
def main():
    # Menu
    print("""\n========= MENU =========
    1 -> Add an item
    2 -> Search
    3 -> Exit 
========================""")                              
    while True:
        # User choice on menu
        user = int(input("\nWhat do you want to do?: "))
        # Option 1
        if user == 1:
            print("\n**********************************************************")
            username = input("           Please pick a unique username: ")
            global info
            name = input("\nEnter your name: ")
            age = input("Enter your age: ")
            address = input("Enter your address: ")
            contact = input("Enter your contact number: ")
            info =f"""\nName : {name}
Age : {age}
Address : {address}
Contact Number : {contact}"""
            newcontactinfo = {
                (f"{username}") : info 
            }
            allcontactinfo.update(newcontactinfo)
            print(f"\n========= The username '{username}' has been added successfully! =========")
            main()
        # Option 2    
        elif user == 2:
            find = input("\nPlease enter your username: ")
            for key in allcontactinfo:
                if key == find:    
                    print(f"\n========= Here are all the informations under the username '{find}': =========")
                    print(allcontactinfo.get(find))
                    print("\n==============================================================================")
                    main()
            else:
                print(f"\n========= There is no '{find}' in our system =========")
                main()
        # Option 3
        elif user == 3:
            while True:
                ext = input("\nAre you sure that you want to exit? (y/n): ").lower()
                if ext == "y":
                    print("\nThank you for using the Contact Tracing Program, bye! :)")
                    exit()
                elif ext == "n":
                    main()
                else:
                    continue
        else:
            continue                   
main()
        


