def age_program():
    while True:
        secondsOrYears = input("Seconds S or Years Y ? ")
        if secondsOrYears == "s":
            val = input("enter Seconds : ")
            print("years {} ".format(int(val)/60/60/24/365))
        elif secondsOrYears == "y":
            val = input("enter Years : ")
            print("seconds {} ".format(int(val) *365 *24 *60 *60))
        else:
            print("invalid input")

            
age_program()