class City:
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks

hosur = City("Hosur", "India", 116821, ["Hosur Fort", "Kelavarapalli Reservoir"])
lahore = City("Lahore", "Pakistan", 11126285, ["Badshahi Mosque", "Lahore Fort", "Shalimar Gardens"])

print(vars(hosur))
print(vars(lahore))
