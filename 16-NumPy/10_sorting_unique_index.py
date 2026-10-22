import numpy as np
# np.sort()
# Sorting arranges values in a specified order.
numbers = np.array([50, 10, 40, 20, 30])
result = np.sort(numbers)

print(result)
print(numbers)

result = np.sort(numbers) [::-1]
print(result)

# 2d array
matrix = np.array([
    [30, 10, 20],
    [90, 60, 70]
])
# 2d array sorting
print(np.sort(matrix, axis = 1))