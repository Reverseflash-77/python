import datetime
import bday_messages

today = datetime.date.today()

birthday_month = 4
birthday_day = 5

next_birthday = datetime.date(today.year, birthday_month, birthday_day)

if next_birthday < today:
    next_birthday = datetime.date(today.year + 1, birthday_month, birthday_day)

days_away = (next_birthday - today).days

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f"My next birthday is {days_away} days away!")