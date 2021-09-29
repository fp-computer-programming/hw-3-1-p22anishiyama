# Author: ATN 9/29/21

user_choice = int(input("Enter a number: "))
if(user_choice % 2 == 0):
    print("Your selection " + str(user_choice) + " is a multiple of two.")
if (user_choice % 3 == 0):
    print("Your selection " + str(user_choice) + " is a multiple of three.")
if (user_choice % 5 == 0):
    print("Your selection " + str(user_choice) + " is a multiple of five.")
