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

