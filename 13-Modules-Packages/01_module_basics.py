'''
A module is a Python file containing resuable code, such as variables,
functions and classes. 
We can import that code into another Python file instead of writing everything in one file.
'''
import calculator
print(calculator.add(10, 5))
print(calculator.subtract(10, 2))
print(calculator.multiply(20, 22))

'''
calculator -> module er nam
add - module er function
(10, 5) module er arguments
'''

result = calculator.add(20, 199)
print(result)

# particular function import
from calculator import add
results = add(39, 11)
print(results)

# using alias
import calculator as calc

resultss = calc.multiply(4, 29)
print(resultss)