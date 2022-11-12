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
    print("""\n=========================== MENU ==========================
    1 -> Add an item
    2 -> Search
    3 -> Exit (y/n)
===========================================================""")
    user = int(input("What do you want to do?: "))
    if user == 1:
        username = input("Please pick a unique username: ")
        info = {
            "Name" : input("Enter your name: "),
            "Age" : input("Enter your age: "),
            "Address" : input("Enter your address: "),
            "Contact Number" : input("Enter your contact number: ")
            }
        newcontactinfo = {
            (f"{username}") : info 
        }
        allcontactinfo.update(newcontactinfo)
        print(f"The username {username} has been added successfully!")
        main()
    elif user == 2:
        find = input("Please enter your username: ")
        print(f"Here are the informations under the username {find}: ", allcontactinfo.get(find))
        main()
main()
        


