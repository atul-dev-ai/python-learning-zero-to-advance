'''
An instance method is a function defined inside a class that works with 
an instance's data. Its first parameter is conventionally "self".
'''


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def show_info(self):
        print("Name:", self.name)
        print("Student_id:", self.student_id)

Student1 = Student("Atul Paul", "ST123")
Student2 = Student("Aditiya Paul", "ST124")

Student1.show_info()
print("------------------")
Student2.show_info()

