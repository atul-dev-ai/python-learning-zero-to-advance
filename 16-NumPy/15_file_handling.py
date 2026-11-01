import numpy as np
'''
File handling in NumPy allows to read and write data to and from files, 
making it easier to work with large datasets and store results for later user.
'''

marks = np.array([80, 75, 90, 65, 85, 70, 95, 60])

# save array to a file
# np.save() stores a NumPy array in a binary .npy format, which is efficient for storage and retrieval.
np.save("C:\\Users\\ADMIN\\Documents\\python-learning-zero-to-advance\\16-NumPy\\marks.npy", marks)

print("Array saved successfully to marks.npy")

# load array from a file
# np.load() loads a NumPy array from a binary .npy file, allowing you to retrieve previously saved data. 
marks = np.load("C:\\Users\\ADMIN\\Documents\\python-learning-zero-to-advance\\16-NumPy\\marks.npy")
print("Array loaded successfully from marks.npy")
print("Loaded marks:", marks)

# shape
print("Shape of the array:", marks.shape)