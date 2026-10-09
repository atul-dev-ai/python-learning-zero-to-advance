'''
- Recursion holo emon ekti process ekhane
ekti function nijekei abar call kore.
- Recursion obosshoi kono ek somoy theme jabe.
- je condition Recursion thamay take bole Base Case.
'''
# Simple example
def countdown(n):
    if n == 0:
        return
    print(n)

    countdown (n - 1)

countdown(5)

# Recursion function = Recursive call + Base case.
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n -1)

    print(n)
print_numbers(10)

# With Factorial
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

result = factorial(5)
print(result)

# task 1
def task1(n):
    if n == 0:
        return
    print(n)

    task1(n - 1)

task1(9)

# Task 2
def task2(n):
    if n == 0:
        return
    task1(n - 1)
    print(n)
task2(10)

# Task 3
def task3(n):
    if n == 0:
        return 1

    return n * task3(n - 1)
results = task3(6)
print(results)

# Task 4
def task4(n):
    if n == 0:
        return 0

    return n + task4(n - 1)

result = task4(5)
print(result)

# 1. recursion diye 1 theke n porjonto sum
def calculate_sum(n):
    if n == 0:
        return 0

    return n + calculate_sum(n - 1)
    print(n)
calculate_sum(19)
# print(calculate_sum(5))
'''
The function calls ifself with a smaller number 
until it reaches zero. Then it returns through the previous calls, 
calculating the total.
'''
# 