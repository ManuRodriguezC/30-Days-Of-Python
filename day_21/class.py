
class Classname:
    pass
print(Classname)

class Person:
    pass
print(Person)

p = Person
print(p)
print("\n")

# Class Constructor

class Person:
    def __init__(self, name):
        self.name = name

p = Person('Esteban')
print(p.name)
print(p)

class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

p = Person('Esteban', 'Rodriguez', '27', 'Colombia', 'Madrid')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)

# Object Methods

class Person:
    def __init__(self, name, lastname, age, country, city, pet):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.country =country
        self.city = city
        self.pet = pet
    def person_info(self):
        return f'{self.name} {self.lastname} is {self.age} years old. He lives in {self.country}, {self.city}. He has a pet her name is {self.pet}'
    
p = Person('Esteban', 'Rodriguez', 27, 'Colombia', 'Madrid', 'Milo')
print(p.person_info())

# Object Default Methods

class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
