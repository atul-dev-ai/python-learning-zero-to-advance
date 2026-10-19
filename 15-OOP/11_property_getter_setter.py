'''
Getters and setters help control how an object's attributes are 
accessed and updated. They are useful when we need validation before accepting a new value.
'''

# property diye Getter
class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

student = Student(80)

print(student.marks)


# setter value diye vul value atkano
class Student:
    def __init__(self, marks):
        self.marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError("Marks must be a number")

        if value < 0 or value > 100:
            raise ValueError("Marks must be between 0 and 100")

        self._marks = value


student = Student(80)

print("Initial marks:", student.marks)

student.marks = 95
print("Updated marks:", student.marks)

student.marks = 150
