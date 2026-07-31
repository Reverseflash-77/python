def get_item(item_number):
    if item_number == 1:
        return '🍔 Cheeseburger'
    elif item_number == 2:
        return '🍟 Fries'
    elif item_number == 3:
        return '🥤 Soda'
    elif item_number == 4:
        return '🍦 Ice Cream'
    elif item_number == 5:
        return '🍪 Cookie'
    else:
        return 'Invalid number'

def welcome():
    print("Welcome to McDonalds")

welcome()
option = int(input("What would you like to order? "))
print(get_item(option))