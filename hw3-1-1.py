# Author: ATN 9/28/21

# Scoring:
one_num_wins = input("How many wins Team 1? ")
one_num_ties = input("How many ties Team 1? ")

two_num_wins = input("How many wins Team 2? ")
two_num_ties = input("How many ties for Team 2? ")

one_points = (one_num_wins * 3) + (one_num_ties)
two_points = (two_num_wins * 3) + (two_num_ties)

if (one_points > two_points):
    print("Team 1 finished with more points.")
else:
    print("Team 2 finished with more points.")
