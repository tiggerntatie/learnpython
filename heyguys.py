def the_flying_circus():   
    print ("You're going to die!")
    answer = input("How many apples you eat per day?")
    answer = int()
    if answer > 5:
        print ("You'll live forever!")
    elif answer <= 5 and answer > 0:
        print ("You'll die at a nice round 100 years old.")
    else:
        return True
        print ("You're already dead!")
the_flying_circus()
