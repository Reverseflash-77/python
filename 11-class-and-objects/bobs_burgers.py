from restaurant import Restaurant

bobs_burgers = Restaurant()

bobs_burgers.name = "Bob's Burgers"
bobs_burgers.category = "American Diner"
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

pizza_hut = Restaurant()

pizza_hut.name = "Pizza Hut"
pizza_hut.category = "Pizza"
pizza_hut.rating = 4.3
pizza_hut.delivery = True

kfc = Restaurant()

kfc.name = "KFC"
kfc.category = "Fast Food"
kfc.rating = 4.5
kfc.delivery = True

print(vars(bobs_burgers))
print(vars(pizza_hut))
print(vars(kfc))