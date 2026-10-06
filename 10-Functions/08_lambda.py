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

