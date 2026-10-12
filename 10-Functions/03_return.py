# return sends back the result of a function
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

# If a function does not return any value, it returns None by default.
def greet():
    print("Hello")

result = greet()
print(result) # none

def test():
    print("A")
    return 
    print("B")
test()
# "B" is not printed because the function terminates immediately after encountering return.

def example():
    return 100
    print("Hello")

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

x = add(10, 30)
y = multiply(30, 19)

print(x)
print(y)

def square(number):
    return number * number

print(square(5))

def add(a, b):
    return a + b

def double(number):
    return number * 2

result = add(19, 39)
print(double(result))

def check_number(number):
    if number > 0:
        return "Possitive"
    else:
        return "Negative"
    
result = check_number(9)
print(result)

def calculate_total(math, english, python):
    return math + english + python

total = calculate_total(80, 75, 90)
print("Total", total)

def is_even(number):
    if number % 2 == 0:
        return "True"
    else:
        return "False"
        
numbers = is_even(5)
print(numbers)