# task 1
dog = {}

# task 2
dog = {
    'Name':'Milo',
    'Color':'Black and white',
    'breed':'Border Collie',
    'legs':4,
    'age':5
}

# task 3
student = {
    'first_name':'Esteban',
    'last_name':'Rodriguez',
    'gender':'Man',
    'age':27,
    'marital status':'Married',
    'skills':['Python, C, Java Script, bash'],
    'country':'Colombia',
    'city':'Madrid',
    'address':'Calla 6#24-57'
}
print(student)

# task 4
print("The size of the student directory is", len(student))

# task 5
value_skills = student['skills']
print("The values of the skills is {} and the type of date is {}".format(value_skills, type(student['skills'])))

# task 6
student['skills'].append('React')
student['skills'].append('C#')
print(student['skills'])

# task 7
print("\n")
keys = student.keys()
print(keys)

# task 8
values = student.values()
print(values)

# task 9
lis = student.items()
print(lis)

# task 10
del student['skills']
del student['first_name']
print(student)

# task 11
del student
print(student)