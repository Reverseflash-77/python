height = int(input("Enter the height of the person in cm: "))
credits = int(input("Enter the number of credits the person has: "))

if height >= 137:
    if credits >= 10:
        print("Enjoy the ride!")
    else:
        print("You do not have enough credits.")
else:
    if credits >= 10:
        print("You are not tall enough to ride.")
    else:
        print("You have not met either requirement.")