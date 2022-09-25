age = [22, 19, 24, 25, 26, 24, 25, 24]

# task 1
size_list = len(age)
print(age)
age = set(age)
size_set = len(age)
print(age)
print("The size of the list is {} and the size of the set is {}".format(size_list, size_set))
print("The size of the list is bigger since the list allow to have repeated data")
# task 2
# The string is a set of characters arranged consecutivety
# A list is usually a data string of the same type, these do not allow repeated characters and these can be manipulated or modified
# A tuple is a string of data that cannot be altered or modified, it can be of the same or different data types.
# A set is a string of data taht have a dates differents types.
# task 3
word = "I am a teacher and I love to inspire and teach people."
word_list = word.split(' ')
print(word)
print(word_list)
word_set = set(word_list)
print(word_set)