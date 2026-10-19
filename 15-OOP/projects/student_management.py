class Person:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, student_id, marks):
        super().__init__(name)
        self.student_id = student_id
        self.__marks = []
        self.marks = marks

    @property
    def marks(self):
        return self.__marks.copy()

    @marks.setter
    def marks(self, new_marks):
        if not isinstance(new_marks, list):
            raise TypeError("Marks must be a list")
        for mark in new_marks:
            if not isinstance(mark, (int, float)) or isinstance(mark, bool):
                raise TypeError("Each mark must be a number")

            if not 0 <= mark <= 100:
                raise ValueError("Marks must be between 0 and 100")

        self.__marks = new_marks.copy()

    def calculate_total(self):
        return sum(self.__marks)

    def calculate_average(self):
        if len(self.__marks) == 0:
            return 0

        return self.calculate_total() / len(self.__marks)

    def show_info(self):
        super().show_info()

        print("Student_ID:", self.student_id)
        print("Marks:", self.marks)
        print("Total:", self.calculate_total())
        print("Average:", self.calculate_average())

Student1 = Student("Atul Paul", "ST123", [80, 70, 90, 99])
Student1.show_info()
print("\nUpdaing marks.....")
Student1.marks = [90, 85, 95, 80]
Student1.show_info()
