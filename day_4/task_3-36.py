# task 3
company = 'Coding For All'
# task 4
print(company)
# task 5
print(len(company))
# task 6
print(company.upper())
# task 7
print(company.lower())
# task 8
print(company.capitalize())
print(company.title())
print(company.swapcase())
# task 9
slice_company = company[7:]
print(slice_company)
# task 10
word = 'Coding'
print(company.find(word))
# task 10
print(company.replace('Coding', 'Python'))
# task 12
print(company.replace('Coding', 'Everyone to Python'))
# task 13
print(company.split())
# task 14
startabs = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(startabs.split(','))
# task 15
sub_0 = company[0]
print(sub_0)
# task 16
last_l = company[-1]
print(last_l)
# task 17
letter_pos_10 = company[10]
print(letter_pos_10)
# task 18
word = "Python For Everyone"
print(word)
str_1 = word[0:6]
str_2 = word[-9:]
print(str_1 + str_2)
# task 19
print(company[0:4] + company[-3:])
# task 20
print(company.index('C'))
# task 21
print(company.index('F'))
# task 22
phrase = "Coding For All People"
print(phrase.rfind("l"))
# task 23
word = "You cannot end a sentence with because because because is a conjunction"
print(word.find("because"))
# task 24
print(word.rindex("because"))
# task 25
word = 'You cannot end a sentence with because because because is a conjunction'
print(word.strip('because'))
# task 26
print(word.find('because'))
# task 27
print(word.strip('because'))
# task 28
substring = "Coding"
print(company.startswith(substring))
# task 29
print(company.startswith("coding"))
# task 30
company = '   Coding For All      '
print(company)
print(company.strip(' '))
# task 31
str_1 = "30DaysOfPython"
str_2 = "thirty_days_of_python"
print(str_1.isidentifier())
print(str_2.isidentifier())
# task 32
librarys = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(librarys))
# task 33
print("I am enjoying this challenge.\nI just wonder what is next.")
# task 34
print("Name\t\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinlad\tHelsinki")
# task 35
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square" .format(radius, area))
# task 36

a, b = 8, 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b ,a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))