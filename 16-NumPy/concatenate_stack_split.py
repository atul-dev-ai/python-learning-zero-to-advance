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
result = np.vstack((a, b))
print(result)
print(result.shape)