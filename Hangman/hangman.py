import random

name = input("What is your name? -->")
if not name:
    print("Please enter your name!") 
    exit()
print("Good Luck ! " + name)

words = ['rose','red','elephant','loop','timeline']

hidden_word = random.choice(words)

print("----Hangman----")
guess_word = ''
guess_count = 5

try:
    while(guess_count > 0):
        try_count = 0
        for char in hidden_word:
            if (char in guess_word):
                print(char)
            else:
                print("_")
                try_count += 1
        if (try_count == 0):
            print("You win!")
            print("The word is: "+hidden_word)
        guess = input("enter a letter: ")
        guess_word += guess
        if guess not in guess_word:
            guess_count -= 1
            print("wrong!")
            print("You have "+guess_count+" more guesses.")
        if (guess_count == 0):
            print("You Loose!")
except(KeyboardInterrupt):
    print("Game Ended!")
except (ValueError):
    print("please enter a letter")