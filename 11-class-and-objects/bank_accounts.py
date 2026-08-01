class BankAccount:
    def __init__(self,first_name ,last_name ,account_id , account_type, pin ,balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print("The Balance:", self.balance)

user = BankAccount("Reverse"," Flash", 11111, "Saving", 1234, 1000 )

user.deposit(96)
user.withdraw(25)

user.display_balance()