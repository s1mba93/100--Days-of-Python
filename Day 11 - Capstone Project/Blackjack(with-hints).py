#Made with lesson hints
import random
from art import logo
import os

#Functions
def clear():
  os.system('cls' if os.name=="nt" else 'clear')

def deal_cards():
  '''Return a random card'''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_scores(cards):
  '''Return the sum of a cards from given list'''
  #Check for blackjack
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  #Check for A 11 or 1
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)

  

  return sum(cards)

def compare_scores(user_score, computer_score):
  '''Compare users scores to determin winner. Requires all users scores'''
  if user_score == 0:
    return "You have Blackjack! You Win!"
  elif computer_score == 0:
    return "Dealer has Blackjack! You Lose"
  elif user_score > 21 and computer_score > 21:
    return "You Bust. You Lose"
  elif user_score == computer_score:
    return "Its a Draw."
  elif user_score > 21:
    return "You Bust. You Lose"
  elif computer_score > 21:
    return "Dealer Bust. You Win!"
  elif user_score > computer_score:
    return "You scored higher then the dealer. You Win!"
  else:
    "Dealer scored higher. You Lose. "
  
def intilise_game():
    
    print(logo)

    #init hands
    player_cards = []
    dealers_cards = []

    #Deal hands
    while len(player_cards) < 2 and len(dealers_cards) < 2:
      player_cards.append(deal_cards())
      dealers_cards.append(deal_cards())

    end_game = False
    while not end_game:
        player_score = calculate_scores(player_cards)
        dealers_score = calculate_scores(dealers_cards)
        print(f"      Your cards are: {player_cards}, current score is: {player_score}")
        print(f"      Dealers first card is: {dealers_cards[0]}")

        #Check for blackjack
        if player_score == 0 or dealers_score == 0:
            end_game = True
        
        #Check for bust
        if player_score > 21 or dealers_score > 21:
            end_game = True

        #Players Turn
        if input("Type 'Y' to draw another card, type 'N' to pass: ").lower() == "Y":
            player_cards.append(deal_cards())
        else:
            end_game = True
        
        while dealers_score !=0 and dealers_score < 17:
            dealers_score.append(deal_cards())
            dealers_score = calculate_scores(deal_cards)

        print(f"      Your final hand is {player_cards}. You finish with a score of {player_score}.")
        print(f"      Dealers final hand was {dealers_cards}. Their score was {dealers_score}.")
        print(compare_scores(player_score, dealers_score))
    
while input("Do you want to playe a game of Blackjack? Type 'Y' or 'N': ").lower() == "y":
    clear()
    intilise_game()
    
    
  