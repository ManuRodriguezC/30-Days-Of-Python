# Exercises - Day 3

# task 1
age = 27
#task 2
height = 1.78
#task 3
complex = 10j

#task 4
print('\n --- Enter base and height os the triangle --- \n')
base = input('base = ')
height = input('height = ')
area = (1/2 * int(base)) * int(height)
print('The area of the triangle is ', area)

#task 5
print('\n --- Perimeter of the triangle --- \n')
a = input('side a = ')
b = input('side b = ')
c = input('side c = ')
perimeter = int(a) + int(b) + int(c)
print('Perimeter of the triangle is ', perimeter)

# task 6
print('\n --- Dates of triangle --- \n')
length = int(input('length = '))
width = int(input('widht = '))
area = length * width
perimetre = 2 * (length * width)
print('Perimeter of the triangle is ', perimeter)
print('The area of the triangle is ', area)

#Task 7
print('\n---- Radius of the circle ----\n')
pi = 3.1416
radius = int(input('Radius '))
area = pi * radius ** 2
print('The area of the circle is ', area)

# Task 8
print('\n---- Calculate the slope, x-intercept and y-intercept of y = 2x -2 ----\n')
s = 2
print('Slope = ', s)
print('Intercept in x = -2')
print('Intercept in y = 2')

#Task 9
print('\n--- Slope between point (2, 2) and point (6, 10) ----\n')
m = (10 - 2) / (6 - 2)
print('The slope between point (2, 2) and point (6, 10) is ', m)

# Task 10
print('\n-- The slope task 8 and the slope task 9 are same', s == m)

# Task 11
print('\n---- Calculate the value of y in y = x^2 + 6x + 9 where x is igual 0 ---\n')
x = 0
print('Where x is 0 y value is 9' )      

# Task 12
print('\n ---- Comparison statement -----\n')
python = len('python')
dragon = len('dragon')
print('pyton and dragon is same size ', python == dragon)

# Task 13
print('\n--- Use and operator to check if on is found in both python and dragon --\n')
print('on in python and dragon', 'on' in 'python and dragon')

# Task 14
print('\n- I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence. -\n')
print('jargon in I hope this course is not full of jargon', 'jargon' in 'I hope this course is not full of jargon')

# Task 15
print('\n-- There is no on in both dragon and python --\n')
print('on is not dragon and python', 'on' is not 'dragon' and 'python')
print('\n')

# Task 16
size = len('python')
s = float(size)
s_1 = str(size)
print(size)
print(s)
print(s_1)
print('\n')

# Task 17

number_par = 1256
number_impar = 1247
print(number_par % 2)
print(number_impar % 2)
print('\n')

# Task 18  
div = 7 / 3
print(div)
div_2 = int(div)
print(div_2)
print('\n')

# Task 19
print('10 is type ', type(10))
print("'10' is type ", type('10'))
print('\n')

# Task 20
print(type(int(9.8)))
print(type(10))
print('\n')

# Task 21
hours = int(input('How much hours '))
rate = int(input('Rate '))
print('weekly earning is ', rate * hours)
print('\n')

# Task 22
print('\n')
years = int(input('Number of years you have lived '))
seconds = 60 * 60 * 24 * 365
print('You have lived for ', years * seconds, ' seconds')
print('\n')

# Task 23
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')