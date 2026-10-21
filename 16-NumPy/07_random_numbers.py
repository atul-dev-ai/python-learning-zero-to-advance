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

# two dimensional array
numbers = np.random.randint(1, 11, size = (3, 4))
print(numbers)
print(numbers.shape)

numbers = np.random.uniform(10, 20, size=5)
print(numbers)
# uniform() = decimal number 

# np.random.normal() - normal distribution
numbers = np.random.normal(
    loc = 50, # distribution er mean
    scale = 10, # standard deviation
    size = 5
)
print(numbers)

# np.random.default_rng()
rng = np.random.default_rng(42)
numbers = rng.integers(1, 101, size = 5)

print(numbers)

rng1 = np.random.default_rng(42)
rng2 = np.random.default_rng(42)

print(rng1.integers(1, 101, size = 5))
print(rng2.integers(1, 101, size = 5))

# 1. One random integer from 1 to 6
dice = rng.integers(1, 7)
print("Dice:", dice)

# 2. Five random marks from 0 to 100
marks = rng.integers(0, 101, size = 5)
print("Marks:", marks)

# 3. Three random decimal numbers from 10 to 20
prices = rng.uniform(10, 20, size = 3)
print("Prices:", prices)

