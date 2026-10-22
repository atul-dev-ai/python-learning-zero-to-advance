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


# np.argmax()
# np.argmax() returns the index of the maximum value.
index = np.argmax(numbers)
print(index)
print(numbers[index])

index = np.argmax(result)
print(index)
print(result[index])
print(result)

# np.argmin()
index = np.argmin(numbers)
print(index)
print(numbers[index])
print(numbers)

index = np.argmin(result)
print(index)
print(result[index])
print(result)

# np.argsort()
print(numbers)
print(result)
print(np.sort(numbers))
print(np.argsort(numbers))
# sort and argsort of unique values
print(np.sort(result))
print(np.argsort(result))

indices = np.argsort(numbers)
print(numbers[indices])

marks = np.array([75, 92, 68, 92])

# practice
print("Sorted marks:", np.sort(marks))
print("Unique Marks:", np.unique(marks))
print("Highest Marks:", np.max(marks))
print("Highest mark index:", np.argmax(marks))
print("Sorting indexes:", np.argsort(marks))
print("Lowest marks:", np.min(marks))
print("Lowest mark indexes:", np.argmin(marks))
