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


# calculate using method
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0

        return self.calculate_total / len(self.marks)

Student1 = student ("Atul Paul", [80, 90, 99, 89, 85])
print("Name:", Student1.name)
print("Total:", Student1.calculate_total())
print("Average:", Student1.calculate_average())

