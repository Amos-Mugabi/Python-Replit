#seconds calculator

totaldays = int(input("How many days are in this year?"))
day = 24 * 60 * 60

year = 365 * day
leapyear = 366 * day

if totaldays == 366:

    print("There are ", leapyear, "seconds", "in this year")
else:
    print("There are ", year, "seconds", "in this year")
    
