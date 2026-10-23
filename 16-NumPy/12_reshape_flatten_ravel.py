import numpy as np
'''
The shape attribute describe the size of each dimension, while 
ndim tells us the number of dimensions.
'''
# one dimensional array
a = np.array([10, 20, 30, 40, 50, 60])

print(a)
print("Shape:", a.shape) # (6,) mane ekti dimension e 6 ta elements acche
print("Dimensions:", a.ndim)

# two dimensional array 
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(matrix)
print("Shape:", matrix.shape) # (2, 3) mane 2ta row, 3ta column ache
print("Dimensions:", matrix.ndim)

# reshape()
reshape_a = a.reshape(2, 3)
print(reshape_a)
print("Dimension:",reshape_a.ndim)
print(reshape_a.shape)
print(a.reshape(3, 2))
print(a.reshape(6, 1))
print(a.reshape(1, 6))

# reshape(-1)
result = matrix.reshape(-1)
print(result)
print(result.shape)

# flatten() returns a one dimensional copy of the array.
flat = matrix.flatten()
print(flat)
flat[0] = 999
print("Flattened:", flat)
print(flat.shape)
print("Original:", matrix)

# ravel()
# ravel( 0 array ke 1D kore. tobe eti sombob hole view return kore, proyojone copy 0 toiti korte pare.
flat = matrix.ravel()
print(flat)
print(flat.shape)

print(matrix)
print(matrix.shape)