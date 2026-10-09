'''
Lambda function holo suto, ek line er anonymous function.
Anonymous mane normally er kono nam thake na.
'''
square = lambda x: x * x
print(square(5))

# normal func
def add(a, b):
    return a + b
# call
print(add(10, 20))

# Lambda
add = lambda a, b: a + b
print(add(50, 20))
'''
Lambda syntax:
lambda parameters: expression

ex: lambda d: d * 2
Lambda te return lage na.

'''

double = lambda d: d * 2
print(double(8))

mix = lambda a, b: a + b
print(add(10, 80))

# Square
square = lambda x: x ** 2
print(square(8))

# Subtract
subtract = lambda a, b: a - b
print(subtract(20, 9))

# sorted() + lambda
'''
sorted mane holo kono Iterable er jinish gula 
ke sort kore notun list e return kora.
key= use kore tuple er kon ongsho dekhe sort korbe seta bola hoy.
'''
students = [
    ("Atul", 80),
    ("Ankit", 70),
    ("Anik", 90)
]

students.sort(key=lambda student: student[1])
print(students)

# Dictionary with Lambda
student = {
    "Atul": 89,
    "Ankit": 78,
    "Anik": 90
}

result = sorted(
    student.items(),
    key=lambda item: item[1]
)
print(result)

# Lambda + if-else
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(70))
print(check(9))


'''
map() bebohar kore ekti list/iterable er 
protiti element er upore ekoi function chalano jay.
-> ekoi kaj list er prottek ta item er upore kore.
'''

numbers = [1, 2, 3, 4, 5]
result = []
for number in numbers:
    result.append(number ** 2)

print(result)

results = map(lambda x: x ** 2, numbers)
print(result) # output shorashori list hobe na. Python ekti map object dey.

result1 = list(
    map(lambda c: c **2, numbers)
)
print(result1)

numbers2 = [222, 22, 29, 10, 8]
result2 = list(
    map(lambda d: d ** 2, numbers2)
)
print(result2)

result3 = list (
    map(lambda e: e + 10, numbers2)
)
print(result3)

# names = ["Atul Paul", "Rahim", "Karim"]
# result4 = list(
#     map(lambda f: upper)
# )

'''
filter() selects elements from an iterable based on a condition. 
Only elements for which the function returns True are kept.
'''

numbers3 = [1, 2, 3, 4, 5, 6, 7]
result4 = []
for number in numbers3:
    if number % 2 == 0:
        result4.append(number)
print(result4)

result4 = list(
    filter(lambda x: x % 3 == 0, numbers3)
)
print(result4)

result4 = list(
    filter(lambda x: x > 5, numbers3)
)
print(result4)

odd_numbers = list(
    filter(lambda x: x % 2 != 0, numbers3)
)
print(odd_numbers)


# positive number
numbers4 = [-5, 10, -2, 8, 0, 15, 10, -3, -9, 12]
positive = list(
    filter(lambda x: x > 0, numbers4)
)
print(positive)
print(sorted(positive))

# Negative Numbers
negative = list(
    filter(lambda x: x < 0, numbers4)
)
print(negative)

# Student passed
marks = [35, 80, 45, 90, 25, 70]
passed = list(
    filter(lambda mark: mark >= 40, marks)
)
print(passed)

# names length
names = ["Atul Paul", "Rahim", "Karim", "Sakib"]
result4 = list(
    filter(lambda name: len(name) > 6, names)
)
print(result4)

# String condition
result4 = list(
    filter(lambda name: name.startswith("A"), names)
)
print(result4)

# Dictinary + filter()
students = {
    "Atul Paul": 86,
    "Ankit Paul": 99,
    "Anik Paul": 92,
    "Sakib": 88
}
result = list(
    filter(
        lambda item: item[1] >= 80, students.items()
    )
)
print(result)

# map() + filter()
numbers5 = [1, 2, 12, 10, 8, 6, 7, 5, 9, 4, 11, 3]
even_numbers = list(
    filter (
        lambda x: x % 2 == 0, numbers5
    )
)
result4 = list (
    map (
        lambda x: x ** 2, even_numbers
    )
)
print(even_numbers)
print(result4)

result4 = sorted(numbers5)
print(result4)

result4 = sorted(numbers5, reverse=True)
print(result4)

# map() + filter() + sorted()
passed = filter(
    lambda mark: mark >= 6, numbers5
)
passed = list(passed)
print(passed)
bonus = list (
    map (
        lambda mark: mark + 5, passed
    )
)
print(bonus)
result = sorted(bonus)
print(result)


result = sorted (
    map (
        lambda x: x + 5,
        filter(lambda x: x >= 5, marks)
    )
)
print(result)

passed = filter (
    lambda item: item[1] >= 60, students.items()
)

bonus = map (
    lambda item: (item[0], item[1] + 5), passed
)

result = sorted (
    bonus,
    key=lambda item: item[1], reverse=True
)
print(result)

