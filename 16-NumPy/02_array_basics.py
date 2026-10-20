import numpy as np

# create an array
numbers = np.array([10, 20, 30, 40, 50])
print("Array is:", numbers)

# check array type 
print("Type of numbers:", type(numbers))

# check numbers of elements
print("Size of numbers:", numbers.size)

# check array dimensions
print("Checking array dimensions", numbers.ndim)

# check array shape 
print(numbers.shape)

# ndarray = N-dimensional array

# one dimensional array
marks = np.array([70, 80, 90, 60, 100])
# calculate sum 
print("Total:", np.sum(marks))

# calculate average
print("Average:", np.mean(marks))

# calculate highest
print("Highest:", np.max(marks))

# calculate lowest
print("Lowest:", np.min(marks))
