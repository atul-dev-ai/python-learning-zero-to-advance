'''
The shape attribute returs the size of an array along each dimension.
'''
import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60])

# one dimensional array shape
print(numbers.shape)

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# two dimensional array shape
print(matrix.shape)

# Reshape
'''
The reshape() method changes the dimensions of an array without changing its elements, 
provided the new shape is compatible with the number of elemtns.
'''

