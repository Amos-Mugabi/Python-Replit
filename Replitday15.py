# loops and if statements
exit = "no"
while exit == "no":
    animal_sound = input("What animal sound do you want to hear?: ")
    if animal_sound == "cow":
        print("umm.. that goes mooo")
    elif animal_sound == "dog":
        print("ooh that goes rororo")
    elif animal_sound == "sheep":
        print("ugh that goes babaa")
    else:
        print("Sorry, try again.")
    exit = input("Do you want to quit?: ")
