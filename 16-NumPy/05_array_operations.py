import numpy as np
'''
NumPy supports element-wise arithmetic operations on arrays, 
allowing calculations to be applied to corresponding elements.
'''
numbers = np.array([10, 20, 30, 40, 50])
print(numbers + 5)
print(numbers - 5)
print(numbers * 2)
print(numbers / 2)


# corresponding element arithmetic operations
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# comparison operations
'''
Comparison operations compare array elements and 
return Boolean values: True or False
'''
