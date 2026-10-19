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
