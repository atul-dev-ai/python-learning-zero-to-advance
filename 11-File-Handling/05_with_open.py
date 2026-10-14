file = open("/home/atul/Documents/python-learning-zero-to-advance/11-File-Handling/students.txt", "r")

content = file.read()
print(content)

file.close() # In the traditional approach, we need to close the file manually after using it.

# with open()
'''
The with open() statement automatically closes the file when the 
block finishes, even if an exception occurs.
'''

with open("/home/atul/Documents/python-learning-zero-to-advance/11-File-Handling/students.txt", "r") as file:
    content = file.read()
    print(content)
'''
- with -> file use er jonno ekti context toiri kore.
- open(" ", "r") -> file ta read mode e khule.
- as file -> khula file tike file nam er variable e rakhe.
- file.read() -> file er sob lekha pore.
- print(content) sob lekha dekhay.
** with block sesh holei file nije thekei bondho hoye jay.
'''

