# Author: ATN 9/28/21

card_one = input("What is your first card's value? ")
card_two = input("What is your second card's value? ")

if(int(card_one) + int(card_two) < 21):
    print("You are safe.")
else:
    print("You are not safe.")
