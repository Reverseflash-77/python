age = int(input("How old are you? "))
if age >= 18:
    has_license = input("Do you have a valid driver's license? (yes/no) ").strip().lower()
    if has_license == "yes":
        own_car = input("Do you own a car? (yes/no) ").strip().lower()
        if own_car == "yes":
            print("You can drive your own car.")
        else:
            print("You can drive, but you don't own a car.")
    else:
        print("You need a valid driver's license to drive.")
else:
    print("You are too young to drive.")