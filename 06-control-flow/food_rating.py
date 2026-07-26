rating = float(input("Enter your food rating (0-5): "))

if rating < 0 or rating > 5:
    print("Invalid rating. Please enter a number between 0 and 5.")
else:
    if rating > 4.5:
        print("Perfection")
    elif rating > 4:
        print("Excellent")
    elif rating > 3:
        print("Good")
    elif rating > 2:
        print("Fair")
    else:
        print("Poor")