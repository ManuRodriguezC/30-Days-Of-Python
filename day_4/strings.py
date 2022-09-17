# Day 4, this day lerning about the strings

letter = 'A'
print(letter)
print(len(letter))
greeting = 'Hello, World!'
print(greeting)
print(len(greeting))
sentence = 'I hoe you are enjoing 30 days of Python Challenge'
print(sentence)

multiline_string = I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.
print(multiline_string)

# String Concatenation

first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name)
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"\n')

# String Formatting

# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s\n' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s\n' % (python_libraries)
print(formated_string) 

# New Style tring Formatting (str.format)

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)

a = 8
b = 4
print('a = {} and b = {}'.format(a, b))
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}\n'.format(a, b, a ** b))

# String Interpolation / f-Strings (Python 3.6+)
a = 4
b = 3
print('a = {} and b = {}'.format(a, b))
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}\n')

# Python Strings as Sequences of Characters

language = 'Python'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Reversing a string
greeting = 'Hello, World!'
print(greeting[::-1]) 

# String Methods

# Capitalize: Converts the first character of the string to capital letter
challenge = 'thirty days of python'
print(challenge.capitalize())

# count: 
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`

#endswith: Check if a string ends with a specific ending
challenge = 'thirty days of python'
print(challenge.endswith('on'))
print(challenge.endswith('tion'))

# expandtabs: Replaces tab character with spaces, defaul tab size is 8. it takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

#find(): Returns the index of the first occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.find('y'))  # 16
print(challenge.find('th')) # 17

#rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
print('\n')
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 5
print(challenge.rfind('th')) # 1


# rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8
print(challenge.rindex(sub_string, 9)) # error

# isalnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# isdecimal(): Checks if all characters in a string are decimal (0-9)
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed

# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True

# isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnu

# isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

# islower(): Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper(): Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

# join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

# strip(): Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

# replace(): Replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('thirty', 'every'))

# split(): Splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

# title(): Returns a title cased string
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

# swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False



