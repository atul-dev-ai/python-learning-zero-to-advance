'''
- Recursion is a process where a function calls itself.
- A recursive function must terminate at some point.
- The stopping condition that ends recursion is called the Base Case.
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

# 1. Calculate sum from 1 to n using recursion
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
# Calculate power of a number using recursion
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)
print(power(2, 4))

# Calculate sum of digits using recursion
def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)

print(digit_sum(1234))
