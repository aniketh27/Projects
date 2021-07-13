import random

max_number = 6
min_number = 1

roll_die = "yes"

while roll_die == "yes":
    number = random.randint(min_number,max_number)
    if (number == 1):
        print("------")
        print("|  *  |")
        print("------")
    if (number == 2):
        print("------")
        print("|  **  |")
        print("------")
    if (number == 3):
        print("------")
        print("|   *  |")
        print("|  **  |")
        print("------")
    if (number == 4):
        print("------")
        print("|  **  |")
        print("|  **  |")
        print("------")
    if (number == 5):
        print("------")
        print("|*   *|")
        print("|  *  |")
        print("|*   *|")
        print("------")
    if (number == 6):
        print("------")
        print("| *** |")
        print("| *** |")
        print("------")
    roll_die = input("Enter yes if u want to roll again or no to exit:\n")
    if (roll_die == "no"):
        print ("Goodbye! have fun.")
    
