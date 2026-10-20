'''
Indexing is the process of accessing an elemnt at 
a specific position in an array.
'''
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers[0])
print(numbers[4])
print(numbers[-1])

'''
Slicing extracts a portion of an array using a start 
index, stop indexing and optional step.
- start: N index will start from.
- stop: N index will stop at, but the element of this index will not be taken.
- step: How many houses will be taken consecutively.
'''
# start:end
print(numbers[1:4])

# without start 
print(numbers[:3])

# without end 
print(numbers[2:])

# use step only
print(numbers[::2])

# array reverse 
print(numbers[::-2])

# element update
numbers[1] = 90 # index 1 / elemnt 2
print(numbers)

# element update using slicing
numbers[1:3] = [70, 100]
print(numbers)

# two dimensional array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(matrix)

# two dimensional array indexing
print(matrix[0, 0])
print(matrix[1, 2])
print(matrix[2, 1])

