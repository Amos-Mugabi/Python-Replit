# True loop
print("Name the Lyrics")
print()
counter = 1
while True:
  line1 = input("Never going to ------you up.")
  if line1 == "give":
    print("Well done! It took you finally got it.") 
  else:
    print("oh oh another try.")
    counter += 1
  if line1 == "give":
    break
print("Thanks for playing.")
print("You got it in", counter, "attempts.")
