import numpy as np
# Concatenation joins arrays along an existing axis

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])
A = np.array([
    [1, 2],
    [3, 4]
])

B = ([
    [5, 6],
    [7, 8]
])

result = np.concatenate((a, b))
print(result)

# using axis
print(np.concatenate((A,B), axis = 0))
# axis = 0 mane row borabor jokto kora.
print(np.concatenate((a, b), axis = 0))
# axis = 1
print(np.concatenate((A, B), axis = 1))

# np.vstack() - Vertical stacking
# Vertical stacking comines arrays vertically, adding rows.
result = np.vstack((a, b))
print(result)
print(result.shape)

# np.hstack() - Horizontal stacking
# Horizonal stacking comines arrays horizontally.
result = np.hstack((a, b))
print(result)

# np.split()
# Splitting divides an array into multiple sub-arrays
numbers = np.array([10, 20, 30, 40, 50, 60])
parts = np.split(numbers, 3)
print(parts)
