s1_name = "Atul Paul"
s2_name = "Ankit Paul"
s1_attendance = 90
s2_attendance = 77
s1_marks = 88
s2_marks = 65

def calculate_grade(marks):
    if marks >= 80 & marks <= 100:
        return "A+"
    elif marks >= 70 & marks < 80:
        return "A"
    elif marks >= 60 & marks < 70:
        return "A-"
    elif marks >= 50 & marks < 60:
        return "B"
    elif marks >= 40 & marks < 50:
        return "C"
    elif marks >= 33 & marks < 40:
        return "D"
    else:
        return "F"
    
def update_marks(old_marks, new_marks):
    return new_marks

print("Student: ", s1_name)
print("Marks: ", s1_marks)
print("Grade: ", calculate_grade(s1_marks))
print("Attendance: ", s1_attendance)
print()

print("Student: ", s2_name)
print("Marks: ", s2_marks)
print("Grade: ", calculate_grade(s2_marks))
print("Attendance: ", s2_attendance)
print()

s1_marks = update_marks(s1_marks, 99)
print("After updating marks for : ", s1_name)
print("Student: ", s1_name)
print("Marks: ", s1_marks)
print("Grade: ", calculate_grade(s1_marks))
print("Attendance: ", s1_attendance)
print()
