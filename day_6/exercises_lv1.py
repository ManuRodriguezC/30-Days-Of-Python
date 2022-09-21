# EXERCISES LV 1

# task 1
ls = tuple()
# task 2
brothers = ('Sebastian', 'Juan', 'Ernesto', 'David')
sisters = ('Laura', 'Majo', 'Lau', 'Lola')
print(brothers)
print(sisters)
# task 3
all_brothers = brothers + sisters
print(all_brothers)
# task 4
size = len(all_brothers)
print(size)
#task 5
list_family = list(all_brothers)
list_family.append('Martha')
list_family.append('Hernando')
family_members = tuple(list_family)
print(family_members)

# EXERCISES LV 2

# task 1
family_members = list(family_members)
family_members.remove('Sebastian')
family_members.remove('Ernesto')
family_members.remove('Hernando')
family_members.remove('David')
family_members = tuple(family_members)
print(family_members)
print("\n")
# task 2
fruts = ('banana', 'apple', 'cherry', 'watermelon')
vegetebles = ('Lechuga', 'Espinaca', 'zanahoria', 'coliflor')
animals_products = ('Cuero', 'Blood', 'Lana', 'Carne')
food_stuff_tp = fruts + vegetebles + animals_products
print(food_stuff_tp)
# task 3
food_stuff_tp = list(food_stuff_tp)
# task 4
food_stuff_it = food_stuff_tp[:6]
food_stuff_tp = food_stuff_tp[6:]
print(food_stuff_tp)
print(food_stuff_it)
# task 5
food_stuff_it_1 = food_stuff_it[:3]
food_stuff_it_2 = food_stuff_it[3:]
print(food_stuff_it_1)
print(food_stuff_it_2)
# task 6
del food_stuff_tp
# task 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
exit_estonia = 'estonia' in nordic_countries
print(exit_estonia)
exit_iceland = 'Iceland' in nordic_countries
print(exit_iceland)