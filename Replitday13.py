# A University Grading system

print("Exam Grade Calculator")

name = input("Name of exam:")

max = int(input("Max. Possible Score:"))

score = float(input("Your score:"))
result = round(score, 2)

if score >= 90 and score <= 100:
    print("Your grade is A+")
elif score >= 80 and score <= 89:
    print("Your grade is A")
elif score >= 70 and score <= 79:
    print("Your grade is B")
elif score >= 60 and score <= 69:
    print("Your grade is C")
elif score >= 50 and score <= 59:
    print("Your grade is D")
elif score < 50:
    print("Your grade is U")
else:
    print("Try again")

print(
    "You got",
    result,
    "%",
)



