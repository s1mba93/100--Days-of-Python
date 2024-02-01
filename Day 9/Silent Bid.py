from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

def winning_bidder():
  winning_bid = 0
  winner = ""

  for bidders in silent_bidders:
    bid = silent_bidders[bidders]
    if bid > winning_bid:
      winning_bid = bid
      winner = bidders

  print(f"The winner is {winner} with a bid of ${winning_bid}")

silent_bidders = {}
end_bidding = False

print(art.logo)
print("Welcome to the secret auction program.")

while not end_bidding:
  name = input("What is your name: ")
  price = float(input("What is your bid: $"))
  silent_bidders[name] = price

  finished = input('Are there any other bidders? Type "Yes" or "No"\n').lower()
  if finished == "no":
    end_bidding = True
    clear()
    winning_bidder()
  else:
    clear()


