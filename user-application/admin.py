#!/usr/bin/env python3

## Program to Manage User's using Command Line ##
## Version 0.1, Author : Suresh Mandava ###
## Version 0.12 : Handled SQL Error Handling.
## Version 0.13 : Change menu to list details of particular user.
## Version 0.14 : Modules. All code moved into usermod.py
##            : All databases are referenced with sql_db and db_name in library
##            : Added --delete
## Version 0.15 : Update Function now working.
## Version 0.16 : Bugs Search.


# Make sure you set the user.db variable to correct folder #

## Variables.
version=0.14
sql_db = 'data/user.db'

## ---- no code changes below this line ##
import os
import argparse
import user.userapi.models as usermod
import json

""" Default menu prompted during runtime """
def print_menu():       ## Your menu design here
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. List Users")
    print ("2. List User Details")
    print ("3. Add User")
    print ("4. Update User")
    print ("5. Delete User")
    print ("6. Exit")
    print (67 * "-")


""" Take inputs from Menu Validate and execute programs """
def menu_choice():

    loop=True
    while loop:

        print_menu()    # calling print_menu functions

        while True:
          try:
           choice = float(input("Enter your choice [1-5]: "))
           break
          except ValueError:
           print("Oops!  That was no valid number.  Try again...")

        if choice==1:
            print (12 * "-" , "User List" , 12 * "-")
            usermod.list_users(sql_db)
            print (35 * "-")
        if choice==2:
            UserID = input("Enter User ID: ")
            print (12 * "-" , "User Details" , 12 * "-")
            usermod.list_user(sql_db,UserID) ## list user details
            print (35 * "-")
        elif choice==3:
            print (12 * "-" , "Add User" , 12 * "-")
            usermod.add_user(sql_db)
            print (35 * "-")
        elif choice==4:
            print (12 * "-" , "Update User" , 12 * "-")
            usermod.update_user(sql_db,UserID)
            print (35 * "-")
        elif choice==5:
            print (12 * "-" , "Delete User" , 12 * "-")
            usermod.delete_user(sql_db,UserID)
            print (35 * "-")
        elif choice==6:
            print ("Exiting...")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again..")


#### Main ####
usermod.pversion()   # Verify python version

# Ensure database file exists.
if not os.path.isfile(sql_db):
   usermod.init_db(sql_db)  # Initalize database

# Take arguments from command line to give options.
parser = argparse.ArgumentParser(description='User Managment API version 0.14')
parser.add_argument('--list',action='store_true',help='list all users' )
parser.add_argument('--listuser',help='list user details' )
parser.add_argument('--add',action='store_true',help='add user' )
parser.add_argument('--update',help='update user' )
parser.add_argument('--delete',help='delete user' )
parser.add_argument('--menu',action='store_true',help='intractive user mgmt menu' )

args = parser.parse_args()

if args.list:
    result = usermod.list_users(sql_db) ## List userid
    print (json.dumps(result,indent=2))
elif args.listuser:
    UserID=args.listuser
    result = usermod.list_user(sql_db,UserID) ## list user details
    print (json.dumps(result,indent=2))
elif args.add:
    while True:
      try:
       userID = str(input("Enter userid : "))
       break
      except ValueError:
       print("Oops!  That was no valid userid.  Try again...")

    while True:
      try:
       userName = str(input("Enter User Name : "))
       break
      except ValueError:
       print("Oops!  That was no valid name.  Try again...")

    while True:
      try:
       userEmail = str(input("Enter email : "))
       break
      except ValueError:
       print("Oops!  That was no valid email.  Try again...")

    while True:
      try:
       userPhone = int(input("Enter Phone : "))
       break
      except ValueError:
       print("Oops!  That was no valid number. Remove hyphens and Try again...")

    usermod.add_user(sql_db,userID,userName,userEmail,userPhone) ## Add user
elif args.update:
    UserID=args.update
    usermod.update_user(sql_db,UserID) ## Update user details
elif args.delete:
    UserID=args.delete
    usermod.delete_user(sql_db,UserID) ## Delete user
elif args.menu:
    menu_choice()    ## Menu selection.
else:
    print ("User Managment API. Version:%s -h for help" % version)
