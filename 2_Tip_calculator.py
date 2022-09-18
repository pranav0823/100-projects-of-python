#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6

#The result rounded up to 2 decimal places = 33.60

print("Welcome to tip calculator")

bill = float(input("What was the total bill ? $"))

tip = int(input("What percentage tip would you like to give ? (Enter a integer value) "))

people = int(input("How many people to split the bill ? "))

bill_with_tip = (tip / 100) * bill + bill

bill_per_person = bill_with_tip / people

final_amount = "{:.2f}".format(bill_per_person)# final amount is rounded up to 2 decimal points

print(f"Each person should pay ${final_amount}")
