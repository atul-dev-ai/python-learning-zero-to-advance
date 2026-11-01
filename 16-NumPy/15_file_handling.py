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
