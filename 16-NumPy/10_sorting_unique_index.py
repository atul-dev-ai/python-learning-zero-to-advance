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
print(np.sort(matrix, axis = 0))


# np.unique()
# np.unique() returns the distinct values in an array, in sorted order by default
numbers = np.array([10, 20, 30, 10, 20, 40, 30, 50, 60, 40, 70])
result = np.unique(numbers)
print(result)

values, counts = np.unique(numbers, return_counts=True)
print("Values:", values)
print("Counts:", counts)
