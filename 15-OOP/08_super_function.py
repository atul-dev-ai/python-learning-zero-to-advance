# super().__init__()
class Person:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

Student1 = Student("Ankit", 8, "st222")

Student1.show_info()
print("Student ID:", Student1.student_id)
