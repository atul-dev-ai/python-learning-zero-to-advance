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

reshapes = np.array([
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
])

matrixs = reshapes.reshape(3, 4) 
# row - column

print(matrixs)
print(matrixs.shape)


