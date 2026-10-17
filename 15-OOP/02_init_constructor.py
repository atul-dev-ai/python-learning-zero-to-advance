'''
The __init__() method initializes an object when it is created.
It is commonly used to set the object's initial attributes.
'''

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        # ekhane self.name  holo object er attribute.
        # right side er name holo function e pawa value.
'''
self Python ke bujte help kore kon object er attribute set kora hocche. tai student1 er data student1
er songge ebong student2 er data student2 er songge jokto thake.

selt python er reserved keyword noy, tobe instance method e prothom parameter hisebe self use korai traditional rule.
'''

student1 = Student("Atul Paul", "ST123")
student2 = Student("Ankit Paul", "ST124")

print(student1.name)
print(student1.student_id)

print(student2.name)
print(student2.student_id)

