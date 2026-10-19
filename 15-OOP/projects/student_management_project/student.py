class Student:
    def __init__(self, name, student_id, marks):
        self.name = name
        self.student_id = student_id
        self.__marks = marks
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
        if not self.__marks:
            return 0

        return self.calculate_total() / len(self.__marks)

    def get_grade(self):
        average = self.calculate_average()

        if average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 40:
            return "D"
        else:
            return "F"

    def to_dict(self):
        return {
            "name": self.name,
            "student_id": self.student_id,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["student_name"],
            data["marks"]
        )

    def show_info(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Marks:", self.marks)
        print("Total:", self.calculate_total())
        print("Average:", self.calculate_average())
        print("Grade:", self.get_grade())

    '''
    To_dict() converts student information into a dictionary, 
    while from_dict() reconstructs a Student object from that dictionary.
    '''
    