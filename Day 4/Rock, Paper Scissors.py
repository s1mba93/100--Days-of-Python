rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

#Set up options into a list
options = [rock, paper, scissors]

#Generate the CPU and Player options
cpu_choice = options[random.randint(0, 2)]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#Error Catch for invalid number
if player_choice < 0 or player_choice >= 3:
  print("You chose an invalid number. Please restart and choose a valid number. ")
else: 
  #Print Both choices
  player_choice = options[player_choice]
  print(player_choice)
  print(f"\nComputer chose:\n{cpu_choice}")

#Check if game is a draw.
if player_choice == cpu_choice:
  print("Its a Draw")
#If Statements for Player picking rock
elif player_choice == options[0] and cpu_choice == options[1]:
  print("You Lose")
elif player_choice == options[0] and cpu_choice == options[2]:
  print("You Win!")
#If Statements for Player picking paper
elif player_choice == options[1] and cpu_choice == options[0]:
  print("You Win!")
elif player_choice == options[1] and cpu_choice == options[2]:
  print("You Lose")
#If Statements for Player picking scissorsS
elif player_choice == options[2] and cpu_choice == options[0]:
  print("You Lose")
elif player_choice == options[2] and cpu_choice == options[1]:
  print("You Win!")





