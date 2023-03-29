print("One Million To One")
print()

correctNum = 575000
counter = 0
while True:
    guess = int(input("What is your guess?:"))
    if guess < 0:
        print("Number out of scope.")
        exit()
    if guess < correctNum:
        print("Too low")
        counter += 1
    elif guess > correctNum:
        print("Too high")
        counter += 1
    elif guess == correctNum:
        print("Perfect! You got it right 😊 ")
        break
    else:
        print("invalid number")
    print("You took ", counter, "attempts to get the correct answer. ")

