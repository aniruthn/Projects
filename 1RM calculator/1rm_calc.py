import sys

print("Welcome to the 1 Rep Max Calculator.")

num_weight = input("How much weight did you lift? ")
num_reps = input("How many reps of that weight did you do? (12 or under) ")

if int(num_reps) > 12:
    print("Try again with a value in range for the number of reps.")
    sys.exit()

repsToRM = [1,0.95,0.93,0.9,0.87,0.85,0.83,0.8,0.77,0.75,0.7,0.67]
index = int(num_reps)-1

print("Your 1 Rep Max is: " + str(round(float(num_weight)/repsToRM[index])))