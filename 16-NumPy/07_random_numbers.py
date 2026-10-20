'''
A random number is a number generated through a random 
or pseudo random process. It is useful for simulations, testing, 
games and machine learning.
'''
import numpy as np

number = np.random.randint(1, 7)
print(number)
# randint(low, high) low included kinto high included na

# multiple random number 
numbers = np.random.randint(1, 101, size = 5)
print(numbers)
