'''
--------------SCOPE-----------------
Scope defines where a variable can be accessed
and where it cannot.
1. Local Scope
2. Global Scope
'''
# 1. Local Scope
def my_function():
    name = "Atul Paul"
    print(name)
my_function() 
'''
Calling print(name) outside causes an error because 
name exists only within the function's local scope.
Outside the function, Python cannot find the variable name.
'''

# Global Scope
name = "Atul" # Global variable
def my_func():
    print(name)
my_func()

# Global variable naming issue
x = 100 # Global

def test():
    x = 50 # Local
    print(x)

test() # The local "x" inside the function does not replace the global "x".
print(x)

# global keyword
'''
If we want to modify a global variable from inside
a function, we can use the 'global' keyword.'''
count = 0
def increase():
    global count
    count += 1

increase()
print(count)

# python how to find a variable
y = 200
def testing():
    print(y)
    print(x)
testing()
'''
Inside test(), Python looks for variable x in this order:
Rule:
1. Local scope
            if not found:
2. Global scope
            if not found:
    Error (NameError)
Python searches for variables from inside out (innermost scope to outer).
'''

balance = 1000
def deposit(amount):
    global balance
    balance += amount
deposit(500)
print(balance)

bals = 1200
def deposits(bals, amount):
    bals = bals + amount
    return bals
bals = deposits(bals, 500)
print(bals)

'''
1. Local Scope
2. Global Scope
3. global Keyword
4. Nested Function
5. Enclosing Scope
6. nonLocal
7. LEGB Rule
'''
# Nested Function
# A func defined inside another func is called a Nested Function.
def outer():
    def inner():
        print("Hello from inner")
    inner()
outer()

# Enclosing Scope:
# In nested functions, variables in the outer function belong to the Enclosing scope.
def outer():
    name = "this variable is a Enclosing Scope"

    def inner():
        print(name) # name is a variable from the outer function
    inner()
outer()
'''
Python first searches inside inner()'s local scope.
If not found, it checks outer()'s enclosing scope.
When executing print(name) inside inner():
Search order:
1. inner() local scope
2. outer() enclosing scope
3. global scope
4. built-in scope

LEGB -> Local, Enclosing, Global (entire module), Built-in (Python built-ins)
'''

# Local -> Enclosing
def outer():
    z = 20

    def inner():
        print(z)

    inner()
outer()

# nonlocal
def outer():
    s = 12

    def inner():
        s = 1
        print(s)
    inner()
    print(s)
outer()

def outer():
    x = 20

    def inner():
        nonlocal x
        x = 12
    inner()
    print(x)
outer()

def outer():
    x = 10

    def inner():
        nonlocal x
        x += 5
        print(x)
    inner()
outer()

'''
global: Used to modify a global variable inside a function.
nonlocal: Used to modify an enclosing variable from an outer function in a nested function.'''

def counter():
    count = 0

    def increase():
        nonlocal count
        count += 1
        return count
    return increase
my_counter = counter()
print(my_counter())
print(my_counter())
print(my_counter())

# practice
glo_x = 1000
def outer():
    glo_x = 50

    def inner():
        nonlocal glo_x
        glo_x += 19
        print("inner:", glo_x)
    inner()
    print("outer:", glo_x)
outer()
print("Global:", glo_x)