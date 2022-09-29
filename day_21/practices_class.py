class Person:
    def __init__(self, name, age, generus, code):
        self.__name = name
        self.age = age
        self.generus = generus
        self.code = code

    def __str__(self):
        return (f"{self.name} is {self.age} years old. Is a {self.generus} and this code is {self.code}")

    def checker(self, owner):
        if self.age < 30:
            print(f"{self.name} is greater that {owner}")
        else:
            print(f"{self.name} is less that {owner}")
        

class Students(Person):
    def __init__(self, name, age, generus, code, grade):
        Person.__init__(self, name, age, generus, code)
        self.grade = grade
        print(f"{self.name} student successfull registration with the code {self.code}\n")

class Teacher(Person):
    def __init__(self, name, age, generus, code, salary):
        Person.__init__(self, name, age, generus, code)
        self.slaty = salary
        print(f"{self.name} teacher successfull registration with the code {self.code}\n")


T_1 = Teacher('Lola', 35, 'Womna', 10.150, '$ 1000')
T_2 = Teacher('Carlos', 40, 'Man', 10.000, '$2000')
E_1 = Students('Esteban', 27, 'Man', 105, 'Firts')
E_2 = Students('Juan', 24, 'Man', 106, 'Second')
print('\n')
T_1.checker("Manu")
T_2.checker("Manu")
E_1.checker("Manu")
E_2.checker("Manu")

print("\n")
print(T_1)
print(T_2)
print(E_1)
print(E_2)

