file = open("/home/atul/Documents/python-learning-zero-to-advance/11-File-Handling/students.txt", "r")

content = file.read()
print(content)

file.close() # In the traditional approach, we need to close the file manually after using it.

# with open()
'''
The with open() statement automatically closes the file when the 
block finishes'''