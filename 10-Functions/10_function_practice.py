def student_result(name, marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 40:
        status = "Pass"
    else:
        status = "Fail"
    return total, average, status

result = student_result("Atul Paul", [80, 94, 88])
print("Total:", result[0])
print("Average:", result[1])
print("Status:", result[2])