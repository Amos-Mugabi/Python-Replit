# Using a for Loop
print("Loan Calculator")
print()
print("$1000 over 10 years at 5% APR.")
print()
value = 1000
apr = 0.05

for i in range(10):
  value += (value * 0.05)
  print("Year", i+1, "is", round(value, 2))
