#Made using none of the lesson hints
from art import logo
import random

#Global Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Functions
def deal_cards(users_hand):
  '''appends a card to a users hand. Specify whos hand the card needs to be added to'''
  random_card = random.randint(0, len(cards) - 1)
  card = cards[random_card]
  if random_card == 10:
      card = "J"
  elif random_card == 11:
      card = "Q"
  elif random_card == 12:
      card = "K"
  elif card == cards[0]:
      card = "A"
  users_hand.append(card)

def calculate_scores(users_hand, users_score):
  '''Calculate users score and return the value'''
  users_score = 0
  for card in users_hand:
    if card == "K" or card == "Q" or card == "J":
      users_score += 10
    elif card == "A" and users_score <= 21:
        users_score += 11
    elif card == "A" and users_score > 21:
        users_score += 1
    else:
        users_score += card
  return users_score
        
#Intilise loop
end_game = False
while not end_game:
  #Set all variable to 0
  player_cards = []
  player_score = 0
  dealers_cards = []
  dealers_score = 0

  #Deal cards
  while len(player_cards) < 2 and len(dealers_cards) < 2:
      deal_cards(player_cards)
      deal_cards(dealers_cards)
  
  #Calculate intial scores
  player_score = calculate_scores(player_cards, player_score)
  dealers_score = calculate_scores(dealers_cards, dealers_score)        


  print(logo)
  print(f"      Your cards are: {player_cards}, current score is: {player_score}")
  print(f"      Dealers first card is: {dealers_cards[0]}")

  #Begin players turn
  player_turn = True
  while player_score <= 21 and player_turn == True:
    hit_stick = input("Type 'Y' to get another card, type 'N' to pass: ").lower()
    if hit_stick == "y":
      deal_cards(player_cards)
      player_score = calculate_scores(player_cards, player_score)
      print(f"      Your cards are: {player_cards}, current score is: {player_score}")
      print(f"      Dealers first card is: {dealers_cards[0]}")
    else:
      player_turn = False
  #Check if player bust and if not begin dealers turn    
  if player_score <= 21:
    dealers_turn = True
    while dealers_score <= 21 and dealers_turn == True:
      if dealers_score < 17:
        deal_cards(dealers_cards)
        dealers_score = calculate_scores(dealers_cards, dealers_score)
      elif dealers_score <= 21:
        dealers_turn = False
  elif player_score > 21:
    print(f"      You bust with a score of {player_score}. Your final hand is {player_cards}")
    print(f"      Dealers score is {dealers_score}. Their final hand was {dealers_cards}")
    print("Dealer Wins")
  elif player_score <= 21 and dealers_score > 21:
    print(f"      Your finshed with a score of {player_score}. Your final hand is {player_cards}")
    print(f"      Dealers score is {dealers_score}. Their final hand was {dealers_cards}")
    print("Player wins!")

    #Work out final winner if no one bust. 
  if player_score < dealers_score:
    print(f"      You finish with a score of {player_score}. Your final hand is {player_cards}")
    print(f"      Dealers score is {dealers_score}. Their final hand was {dealers_cards}")
    print("Dealer Wins")
  elif player_score == dealers_score:
    print(f"      You finish with a score of {player_score}. Your final hand is {player_cards}")
    print(f"      Dealers score is {dealers_score}. Their final hand was {dealers_cards}")
    print("Its a Draw")

  
  if input("Do you want to player again? Type 'Y' or 'N'").lower() == "n":
    end_game = True