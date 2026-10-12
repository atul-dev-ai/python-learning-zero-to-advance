file = open("/home/atul/Documents/python-learning-zero-to-advance/11-File-Handling/students.txt", "r")
content = file.read()

print(content)
file.close()


# full file read
file = open("/home/atul/Documents/python-learning-zero-to-advance/11-File-Handling/students.txt", "r")
print(file.read())
file.close

# readline()
file = open("/home/atul/Documents/python-learning-zero-to-advance/11-File-Handling/students.txt", "r")
print(file.readline())
print(file.readline())
print(file.readline())

file.close()

file = open("/home/atul/Documents/python-learning-zero-to-advance/11-File-Handling/students.txt", "r")

lines = file.readlines()
print(lines)
file.close