import random
import os
from art import logo

end_program = False

def clear():
  '''Clears the console'''
  os.system('cls' if os.name=="nt" else 'clear')

def difficulty_level(difficultly_choice):
    '''Returns the number of lives based on the users choice.'''
    if difficultly_choice == "easy":
        return 10
    elif difficultly_choice == "hard":
        return 5

def random_number_generator(starting_number, end_number):
    '''Returns a random number based on passed in range.'''
    return random.randint(starting_number, end_number)

def intilise_game():
    restart = False
    while not restart:
        clear()
        end_round = False
        lives = 0
        random_number = random_number_generator(1, 100)
        print(logo)
        lives = difficulty_level(input("Choose a difficulty level. Type 'Easy' or 'Hard': ").lower())
        clear()
        print(logo)
        print("I'm thinking of a number between 1 and 100")
        
        while not end_round:
            if lives > 0:
                print(f"You have {lives} attempts to guess the number.")
                guess = int(input("Make a guess: "))
                if guess < random_number:
                    print(f"Too low.")
                    lives -= 1
                elif guess > random_number:
                    lives -= 1
                    print(f"Too high.")
                elif guess == random_number:
                    end_round = True
                    print(f"You got it! The answer was {random_number}")
            else:
                end_round = True
                print(f"You ran out of lives. The answer was {random_number}.\n\n\n")
        print("Would you like to try again?")
        if input("Type 'Y' to try again, or 'N' to return to the title screen: ").lower() == "y":
            restart = False
        else: 
            restart = True
        
while not end_program:
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    if input("Would you like to try and guess the number I am thinking off? Type 'Y' or 'N': ").lower() == "y":
       intilise_game()
    else:
       end_program = True
