height = int(input("Enter the height of the person in cm: "))
credits = int(input("Enter the number of credits the person has: "))

if height >= 137 and credits >= 10:
    print("Enjoy the ride!")
elif height < 137 and credits >= 10:
    print("You are not tall enough to ride.")
elif height >= 137 and credits < 10:
    print("You do not have enough credits.")
else:
    print("You have not met either requirement.")