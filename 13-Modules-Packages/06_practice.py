import school

# student information
name = school.get_student_name
student_id = school.get_student_id
department = school.get_student_dept

# Students marks
marks = [80, 75, 90, 85]

# calculate result
total = school.calculate_total(marks)
average = school.calculate_avg(marks)
result = school.get_result(average)

# display information
print("Student name:", name)
print("Student ID:", student_id)
print("Departmetn:", department)
print("Marks:", marks)
print("Total marks:", total)
print("Average Marks:", average)
print("Result:", result)

