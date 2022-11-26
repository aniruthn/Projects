from random import seed
from random import random

again = True

while again:
    
    human_choice = input("Enter what you want (rock, paper, or scissors): ")
    print("You selected " + human_choice + ".")

    if human_choice == "paper":
        human_choice = 1
    elif human_choice == "scissors":
        human_choice = 2
    else:
        human_choice = 3

    value = random()*3 + 0.5
    value = round(value)

    if value == human_choice:
        print("I selected that too. Go again?")
    elif (value == human_choice + 1) or (value == 1 and human_choice == 3):
        print("I won!")
        again = False
    else:
        print("You won!")
        again = False
    
    randomVariable = input("Hit enter to go again or to exit.")