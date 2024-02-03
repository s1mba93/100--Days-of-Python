import random
from art import logo, vs
from game_data import data
import os

def clear():
  '''Clears the console'''
  os.system('cls' if os.name=="nt" else 'clear')

def generate_account():
   '''Returns a random account from Game Data'''
   return random.choice(data)   

def format_data(account):
   '''Returns the data from account in a readable format minus the follower count.'''
   ig_name = account["name"]
   ig_description = account["description"]
   ig_country = account["country"]
   ig_follower = account["follower_count"]

   return f"{ig_name}, {ig_description}, from {ig_country}"

def check_answer(choice, account_a, account_b):
   '''Returns 'a' or 'b' depending on who has the highest follow'''
   if choice == "a" and account_a["follower_count"] > account_b["follower_count"]:
      return "correct"
   elif choice == "b" and account_a["follower_count"] < account_b["follower_count"]:
      return "correct"
   else:
      return "incorrect"

def compare_followers(account_a, account_b):
   '''takes two accounts and returns the one with the highest follower count'''
   if account_a["follower_count"] > account_b["follower_count"]:
      return account_a
   elif account_a["follower_count"] < account_b["follower_count"]:
      return account_b

  
def initilise_game():
    end_round = False
    score = 0
    clear()
    print(logo)    
    account1 = generate_account()
    account2 = generate_account()
    # higher_follower = compare_followers(account1, account2)
    while not end_round:
        print(f"Compare A: {format_data(account1)}")
        print(vs)
        print(f"Against B: {format_data(account2)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        clear()
        print(logo)
        if check_answer(guess, account1, account2) == "correct":    
            score += 1
            print(f"You're right! Current score: {score}")
            account1 = compare_followers(account1, account2)
            account2 = generate_account()
        else:
           end_round = True
           print(f"Sorry, that's wrong. Final score: {score}")
           


initilise_game()






