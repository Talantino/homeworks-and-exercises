################The tip calculator project

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $:\n"))
tip = int(input("What percetage would you like to give? 10,12 or 15\n"))
people = int(input("How many people to split the bill?\n"))
total_with_tip = tip / 100 * bill + bill
new_total = total_with_tip / people
final_amount = "{:.2f}".format(new_total)
print(f"Each person should pay ${final_amount}")
