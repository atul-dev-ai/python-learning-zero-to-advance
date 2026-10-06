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
x = 100
def test():
    x = 50
    print(x)

test() # function er bitorer "x" bairer "x" ke replace koreni.
print(x)


