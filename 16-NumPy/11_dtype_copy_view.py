import numpy as np
# dtype specifies the data type of the elements sorted in NumPy array

# dtype
numbers = np.array([10, 20, 30, 40])
print(numbers)
print(numbers.dtype)

# different data type 
a = np.array([10, 20, 30])
b = np.array([1.5, 2.5, 3.5])
c = np.array([True, False, True])
d = np.array(["Python", "NumPy", "Pandas"])

print(a.dtype)
print(b.dtype)
print(c.dtype)
print(d.dtype) # <U6 = Unicode string type

# Declaring data type when creating an array
marks = np.array([10, 20, 30], dtype = np.float64)
print(marks)
print(marks.dtype)

# astype()
# astype() converts an array's elements to a specified data type and returns a converted array
decimal_numbers = numbers.astype(float)
print(decimal_numbers)
print(decimal_numbers.dtype)

# float to integer
prices = np.array([10.9, 20.5, 30.8])
whole_prices = prices.astype(int)
print(whole_prices)
print("Data type of prices:", prices.dtype)
print("Data type of whole_prices:", whole_prices.dtype)
result = numbers.astype(bool)
print(numbers)
print(numbers.dtype)