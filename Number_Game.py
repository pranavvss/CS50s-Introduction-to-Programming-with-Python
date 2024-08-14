#Prompts the user for a level,
#If the user does not input a positive integer, the program should prompt again.
#Randomly generates an integer between 1 and n inclusive, using the random module.
#Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
#If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
#If the guess is larger than that integer, the program should output Too large! and prompt the user again.
#If the guess is the same as that integer, the program should output Just right! and exit.

import random

def main():

    while True:
        level = input("Level: ")
        if level.isdigit() and int(level) > 0:
            level = int(level)
            number = random.randint(1, level)
            guess = input("Guess: ")
            if guess.isdigit():
                guess = int(guess)

                if number == guess:
                    print("Just right!")
                    break
                elif number > guess:
                    print("Too small!")
                    continue
                elif number < guess:
                    print("Too large!")
                    continue
            else:
                continue
        else:
            continue

if __name__ == '__main__':
    main()