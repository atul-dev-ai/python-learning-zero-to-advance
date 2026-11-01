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

# data type 
print("Data type of the array:", marks.dtype)

# dimensions
print("Number of dimensions of the array:", marks.ndim)


names = np.array([
    "Atul",
    "Ankit",
    "Sakib",  
    "Rahul",
    "Hasan",
    "Rahim",
    "Karim",
    "Anik",
])

marks = np.array([85, 35, 65, 45, 90, 80, 60, 50])

ages = np.array([20, 22, 21, 23, 19, 24, 25, 22])

# np.savez
# np.savez() allows you to save multiple NumPy arrays into a single compressed .npz file, making it convenient to store related data together.
np.savez("C:\\Users\\ADMIN\\Documents\\python-learning-zero-to-advance\\16-NumPy\\students.npz", names=names, marks=marks, ages=ages)

print("All arrays saved successfully to students.npz")

# data loading
data = np.load("C:\\Users\\ADMIN\\Documents\\python-learning-zero-to-advance\\16-NumPy\\students.npz")
print("All arrays loaded successfully from students.npz")

print("Loaded names:", data["names"])
print("Loaded marks:", data["marks"])
print("Loaded ages:", data["ages"])

