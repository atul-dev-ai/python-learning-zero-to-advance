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