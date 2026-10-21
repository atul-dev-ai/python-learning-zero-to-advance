'''
A matrix is a rectangular arrangement of numbers in rows and columns.
'''
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a)
print("Shape of a:", a.shape)
print(type(a))

b = np.array([
    [7, 8, 9],
    [10, 11, 12]
])
print("Shape of b:", b.shape)

# matrix addition & subtraction
print(b)
print(a + b)
print(a - b)

# element wise multiplication
print(a * b)

# matrix multiplication with transpose
# The transpose of a matrix swaps its rows and columns
# (m * k) * (k * n)
print(a @ b.T)
print(a.T @ b)

# transpose of a
print("Transpose of a:", a.T)
print("Original shape:", a.shape)
print("Transpose shape of a:", a.T.shape)

# np.dot
print(np.dot(a.T, b))
print(a.T @ b)