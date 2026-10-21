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
# (m * k) * (k * n)
print(a @ b.T)
print(a.T @ b)
