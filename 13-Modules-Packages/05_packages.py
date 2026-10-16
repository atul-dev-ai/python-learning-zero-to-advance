'''
A module is a Python file, whiile a Package organizes related 
modules into a structured directory. Packages maek larger applications easier to maintain.
'''
# school/ -> package folder
# student.py -> student er info niye kaj korbe.
# result.py -> marks & result niye kaj korbe.

# import form package
import school

name = school.get_student_name()
student_id = school.get_student_id()

marks = [80, 95, 70, 85]

total = school.calculate_total(marks)
average = school.calculate_avg(marks)

print("Student:", name)
print("Student ID:", student_id)
print("Total Marks:", total)
print("Total average:", average)