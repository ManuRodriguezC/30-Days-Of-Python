# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# task 1
print(it_companies)
size = len(it_companies)
print("The size of the it_companies is {}".format(size))
# task 2
it_companies.add("Twitter")
print(it_companies)
# task 3
others_companies = {'LG', 'Asus', 'Acer', 'Hp'}
it_companies.update(others_companies)
print(it_companies)
# task 4
it_companies.remove('LG')
print(it_companies)
# task 5
# the remove emply but not delete, but the discard delete all set
