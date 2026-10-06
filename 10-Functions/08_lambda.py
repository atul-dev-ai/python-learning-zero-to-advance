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

