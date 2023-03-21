# using if, elif and else.

from getpass import getpass as input

print("EPIC BATTLE 💪🏻")
print()

print("Select your move(R, P or S)")
move1 = input("Player 1 > ")
print()
move2 = input("Player 2 > ")
print()

if move1 == "R":
    if move2 == "R":
        print("oh its a draw.🤝🏻")
    elif move2 == "P":
        print("ugsh rock is covered by the paper ")
    elif move2 == "S":
        print("rock is chopped by scissor ")
    else:
        print("Invalid move, try again.")

elif move1 == "P":
    if move2 == "P":
        print("oh its a draw.🤝🏻")
    elif move2 == "R":
        print("rock is covered by paper. ")
    elif move2 == "S":
        print("scissor slices the rock. ")
    else:
        print("Invalid move, try again.")

elif move1 == "S":
    if move2 == "S":
        print("oh its a draw. ")
    elif move2 == "P":
        print("scissor cuts the paper ")
    elif move2 == "R":
        print("scissor cuts the rock. ")
    else:
        print("Invalid move, try again.")
