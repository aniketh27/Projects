import random


number = random.randrange(1,50)
while(True):
    guess_number = int(input("Guess the number b/w 1 to 50:\n"))
    if (guess_number == number):
        print ("VOYLA! You guessed it right!")
    elif (guess_number < number):
        print("You guessed the number too low!")
    else:
        print("You guessed the number too high!")
    break
print ("The number was: "+str(number))

