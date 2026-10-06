'''
--------------SCOPE-----------------
Scope mane holo kono variable kothay access kora jabe
ebong kothay kora jabe na.
1. Local Scope
2. Global Scope
'''
# 1. Local Scope
def my_function():
    name = "Atul Paul"
    print(name)
my_function() 
'''
print(name) dile error dibe karon 
name function er local scope er moddhe ache.
function er baire python name khuje pacche na.
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

test() # function er bitorer "x" bairer "x" ke replace koreni.
print(x)

# global keyword
'''
jodi function er bitore theke global variable er
value change korte chai, tokhon global bebohar korte pari.'''
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
ekhane test() er bitore x lekha ache.
Python prothome kothay x khujbe.
Rule:
1. Local scope
            na paile
2. Global scope
            na paile
    Error(NameError)
Python normally betor theke baire variable khuje.
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
# Nested func er khetre bairer func er variable ke Enclosing scope bola hoy.
def outer():
    name = "this variable is a Enclosing Scope"

    def inner():
        print(name) # name outer er variable
    inner()
outer()
'''
Python prothome inner() er local scope e khujbe.
na pele bairer outer() function er scope e khujbe.
inner() er moddhe print(name)
prothome khujbe:
1. inner() er local scope
2. outer() er enclosing scope
3. global scope
4. built-in scope

LEGB -> Local Enclosing Global(full program) Built-in(Python er built-ing)
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
global = Global variable change korte use kora hoy.
nonlocal = nested func er bairer func er variable change korte use kora hoy.'''

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