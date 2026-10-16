'''
A custom module is a Python file that we create to
organize reusable code. We can import its functions, variables 
and classes into other Python files.
'''
import student_utils

# Custom module import from other file 
name = "Atul Paul"
marks = [
    80,
    75, 
    90,
    85
]

print(student_utils.greet_student(name))
print(student_utils.calculate_total(marks))
print(student_utils.calculate_average(marks))

print(student_utils.university_name)

import greetings
import greetings
greetings.say_hlw()