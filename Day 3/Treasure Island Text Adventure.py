print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
event1 = input("You come to a fork in the road. Do you choose to go left or right\n").lower()

if event1 == "left":
  print("you continue down the left path and come to a wide fast flowing river. You know that you need to cross it. On the other side you can see a boat.")
  event2 = input("Do you choose to wait or swim?\n").lower()
  if event2 == "wait":
    print("You wait a short time for the boat to arrive. It takes you safely across the river.")
    print("further down the road, you come across a small square building with 3 doors. A red one, A blue one and a yellow one.")
    print("on a sign in front of the building it reads:\n")
    print('''
    Before you, three doors stand tall,
    One hides flames that fiercely call.
    Another guards a mimic's snare,
    Ready to catch you unaware.
    The last one holds a treasure rare,
    A gift of gold beyond compare.

    One question to guide your fate,
    A puzzle to navigate.
    Speak, and make your choice sincere,
    Which door holds what you hold dear?

    In queries three, the truth is told,
    A riddle's challenge to unfold.
    Choose wisely now, and make your plea,
    Which colored door shall set you free?
    ''')
    event3 = input("which door do you choose?\n").lower()
    if event3 =="yellow":
      print('''
      The golden door, a gleaming prize,
      Beyond, a treasure that never lies.
      Choose the yellow, fortune's hold,
      A realm of riches, a tale untold.
      ''')
      print("You Won! Now go and enjoy your new fortune!")
    elif event3 =="blue":
      print('''
      Behind the blue, a mimic grins,
      A cunning trap, where danger begins.
      Its jaws await, a lurking snare,
      Choose not blue, for life to spare.
      ''')
      print("GAME OVER")
    elif event3 == "red":
      print('''
      A fiery fate awaits the bold,
      Through the red door, the story's told.
      Flames embrace, a deadly spree,
      You choose the red, and cease to be.
      ''')
      print("GAME OVER")
    else:
      print("You chose a door that does not exist")
      print("GAME OVER")
  else:
    print("You try attempt to swim across but are dragged under by the currents. Unable to break free you drown")
    print("GAME OVER")
else:
  print("You are attacked by a wild boar and are killed.")
  print("GAME OVER")
