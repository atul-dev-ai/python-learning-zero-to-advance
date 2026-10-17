'''
An instance attribute belongs to a specific object. Different objects can have 
different objects can have different values for the same instance attribute.
'''

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

Student1 = Student("Atul Paul", "ST123")
Student2 = Student("Aditiya Paul", "ST124")

print(Student1.name)
print(Student2.name)

print(Student1.student_id)
print(Student2.student_id)

'''
A class attribute is defined inside a class and is shared through the 
class unless an instance has an attribute with the same name.
'''

class Student:
    university = "Daffodil International University"
    # ekhane university class er attribute karon eti class er moddhe directly lekha hoyche, self er maddhome na.
    def __init__(self, name):
        self.name = name # eta instance attribute

Student1 = Student("Anik")
Student2 = Student("Rahim")

print(Student1.name)
print(Student2.name)

print(Student1.university)
print(Student2.university)

Student.university = "Other university"
print(Student1.university)

Student1.university = "Another University"
print(Student1.university)
print(Student2.university)

