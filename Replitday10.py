# calculator

print("Tip Calculator")
print()

total = float(input("How much did you spend?"))
tip = int(input("What percentage do you want to tip?"))
people = int(input("How many people are in your group?"))

tipsum = (15 / 100) * total
newtotal = tipsum + total

amount = newtotal / people
newamount = round(amount, 2)

print("You each owe", newamount)
