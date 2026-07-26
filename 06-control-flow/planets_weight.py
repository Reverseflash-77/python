earth = float(input("Enter your weight on Earth (in kg): "))
planet = int(input("Enter the planet number (1-8): "))
if planet == 1:
    weight = earth * 0.38
    print(f"Your weight on Mercury is: {weight:.2f} kg")
elif planet == 2:
    weight = earth * 0.91
    print(f"Your weight on Venus is: {weight:.2f} kg")
elif planet == 3:
    weight = earth * 0.38
    print(f"Your weight on Mars is: {weight:.2f} kg")
elif planet == 4:
    weight = earth * 2.53
    print(f"Your weight on Jupiter is: {weight:.2f} kg")
elif planet == 5:   
    weight = earth * 1.07
    print(f"Your weight on Saturn is: {weight:.2f} kg")
elif planet == 6:
    weight = earth * 0.89
    print(f"Your weight on Uranus is: {weight:.2f} kg")
elif planet == 7:
    weight = earth * 1.14
    print(f"Your weight on Neptune is: {weight:.2f} kg")
else:
    print("Invalid number")