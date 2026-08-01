class Pokemon():
    def __init__(self,entry,name,types,description,is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(self.name)
        print(self.name)

    def display_details(self):
        print(f'''
Entry Number: {self.entry}
Name: {self.name}
Type: {self.types}
Description: {self.description}''')
        if self.is_caught:
            print(f"{self.name} has already been caught!")
        else:
            print(f"{self.name} has not been caught yet!")

pokemon_card = Pokemon(25, "Pikachu", "Electric" , "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.", True)

pokemon_card.speak()
pokemon_card.display_details()