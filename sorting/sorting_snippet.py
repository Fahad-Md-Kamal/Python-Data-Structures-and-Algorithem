# numbers = [6,9,3,1]

# print(sorted(numbers))
# print(numbers)
# numbers.sort()
# print(numbers)

# words = ['banana', 'pie', 'Washington', 'book']

# # print(sorted(words, key=len, reverse=True))

# # def reverse_word(word):
# #     return word[::-1]

# print(sorted(words, key=lambda x: x[::-1]))

from collections import namedtuple

StudentFinal = namedtuple('StudentFinal', 'name grade')

bill = StudentFinal('Bill', 90)
patty = StudentFinal('Patty', 94)
bart = StudentFinal('Bart', 89)

students = [bill, patty, bart]

print(sorted(students, key=lambda x: getattr(x, 'grade'), reverse=True))
