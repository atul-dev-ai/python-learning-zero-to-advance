file = open("/home/atul/Documents/python-learning-zero-to-advance/11-File-Handling/students.txt", "r")
content = file.read()

print(content)
file.close()


# full file read
file = open("/home/atul/Documents/python-learning-zero-to-advance/11-File-Handling/students.txt", "r")
print(file.read())
file.close