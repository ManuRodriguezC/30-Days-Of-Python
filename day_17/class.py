# Exception Handling
"""
try:
    print(10 + '5')
except:
    print('No se pueden sumar int y str')
"""
"""
try:
    name = input('Enter your name: ')
    year_born = input('Year your were born: ')
    age = 2022 - year_born
    print(f"You are {name}. And your age is {age}.")
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')
"""

# Packing and Unpacking Arguments in Python

# Unpacking
def sum_of_five_numbers(a, b, c, d, e):
    return a + b + c + d + e

lis = [1, 2, 3, 4, 4]
print(sum_of_five_numbers(*lis))

numbers = range(2, 7)
print(list(numbers))
args = [2, 7]
numbers = range(*args)
print(numbers)

# Packing lists
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))        
print(sum_all(1, 2, 3, 4, 5, 6, 7))

# Packing Dictionaries
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
	# Printing dictionary items
    for key in kwargs:
        print("{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))

# Spreading in Python
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      

# Unpacking Dictionaries
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct))

for index, item in enumerate([20, 30, 40]):
    print(index, item)

for index, i in enumerate(countries):
    print(index, i)
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')