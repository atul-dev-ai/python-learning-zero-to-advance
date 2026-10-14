'''
Append mode adds new content to the end of a file without overwriting
its existig content.
If the file does not exist, Python creates it.
'''
with open("/home/atul/Documents/python-learning-zero-to-advance/11-File-Handling/students.txt", "a") as file:
    file.write("Anik Paul\n")

with open("/home/atul/Documents/python-learning-zero-to-advance/11-File-Handling/students.txt", "r") as file:
    content = file.readlines()
    print(content)

# student registration simple practice
student_name = input("Enter Student Name: ")
with open("/home/atul/Documents/python-learning-zero-to-advance/11-File-Handling/students.txt", "a") as file:
    file.write(student_name + "\n")
print("Student added successfully!")
