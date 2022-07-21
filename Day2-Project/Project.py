# Day2 Project - Tip Calculator

# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print("*** Welcome to the Tip Calculator! ***")

bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

# converting tip to percentage
tip_as_percent = tip / 100

# calculating the total tip
total_tip = bill * tip_as_percent

# calculating the total bill
total_bill = bill + total_tip

# calculating amount as bill per person
bill_per_person = total_bill / people
amount = round(bill_per_person, 2)

print(f"Each person should pay: ${amount}")