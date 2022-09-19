# task 1
lista = []
# task 2
sports = ['soccer', 'basketball', 'baseball', 'climb', 'f1']
# task 3
print(len(sports))
# task 4
print(sports[0])
print(sports[2])
print(sports[-1])
# task 5
mixed_data_types = ['Esteban', '27', '1.79', 'Married', 'Calle 6 Sur # 24-57']
# task 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# task 7
print(it_companies)
# task 8
print(len(it_companies))
# task 9
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])
# task 10
it_companies[0] = 'Meta'
print(it_companies)
# task 11
it_companies.append('TI')
print(it_companies)
# task 12
it_companies.insert(4, 'TI')
print(it_companies)
# task 13
it_companies[2] = it_companies[2].upper()
print(it_companies)
# task 14
chang = ['#;']
it_companies.extend(chang)
print(it_companies)
# task 15
does_exist = 'Facebook' in it_companies
print("Facebook is in it_companies: ", does_exist)
# task 16
it_companies.sort()
print(it_companies)
# task 17
it_companies.reverse()
print(it_companies)
# task 18
del it_companies[0:3]
print(it_companies)
# task 19
it_companies_lasts = it_companies[-3:]
print(it_companies_lasts)
# task 20
it_companies_mid = it_companies[2:5]
print(it_companies_mid)
# task 21
it_companies.pop(0)
print(it_companies)
# task 22
it_companies.pop(3)
print(it_companies)
# task 23
it_companies.pop(-1)
print(it_companies)
# task 24
it_companies.clear()
print(it_companies)
# task 25
del it_companies
# task 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end)
print(back_end)
full_stack = front_end + back_end
print(full_stack)
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)