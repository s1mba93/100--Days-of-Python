#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇



print("Welcome to the tip calculator")

total_bill = input("What was the total bill? $")
total_tip = input("What percentage would you like to tip?")
people = input("How many people to split the bill?")

percentage = (float(total_tip) / 100) + 1
bill_with_tip = float(total_bill) * percentage
split_price = round(bill_with_tip / int(people), 2)


print(f"Each person should pay: ${split_price}.")