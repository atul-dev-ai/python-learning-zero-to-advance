import numpy as np
'''
Broadcasting is a NumPy mechanism that allows arithmetic operations 
between arrays of different but compatible shapes.
'''

# example - 1
prices = np.array([100, 300, 200])
result = prices + 5
'''
NumPy adds 5 to every element of the array without requiring us to write a loop.
'''
print(result)

# array add with matrix
marks = np.array([
    [60, 70, 80],
    [50, 65, 75]
])

bonus = np.array([5, 10, 15])

print("Marks shape:", marks.shape)
print("Bonus shape:", bonus.shape)

result = marks + bonus
print(result)

'''
Two dimensions are compatible for broadcasting when they are equal or 
when either dimension is 1. Missing leading dimensions are treated as 1.
'''

# Column Broadcasting
bonus = np.array([10, 20])
column_bonus = bonus.reshape(2, 1)
print("Bonus Shape:", column_bonus.shape)
print(marks + column_bonus)
