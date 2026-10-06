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
        print(name)
    inner()
outer()
