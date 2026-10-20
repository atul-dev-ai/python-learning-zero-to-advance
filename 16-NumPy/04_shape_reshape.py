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

print(matrixs.reshape(-1))

# np.zeros()
numbers = np.zeros(5)
print(numbers)
# np.zeros() creates an array filled with zeros 
matrixs = np.zeros((2, 3))
print(matrixs)

# np.ones()
numbers = np.ones(5)
print(numbers)

matrix = np.ones((2, 3))
print(matrix)

# np.arange 
'''
np.arange() returns evenly spaced values within a given interval, 
using a specified step size.
'''
numbers = np.arange(1, 10, 2)
print(numbers) # (start, stop, step)

# np.linspace
numbers = np.linspace(0, 10, 5)
print(numbers)