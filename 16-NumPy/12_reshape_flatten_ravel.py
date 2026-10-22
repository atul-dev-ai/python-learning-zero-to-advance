import numpy as np
'''
The shape attribute describe the size of each dimension, while 
ndim tells us the number of dimensions.
'''
# one dimensional array
a = np.array([10, 20, 30, 40, 50, 60])

print(a)
print("Shape:", a.shape)
print("Dimensions:", a.ndim)

# two dimensional array 
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
