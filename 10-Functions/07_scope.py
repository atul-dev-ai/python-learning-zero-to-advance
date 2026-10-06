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
