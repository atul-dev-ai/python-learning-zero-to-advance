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

# with *args
def calculate_total(*marks):
    total = 0

    for mark in marks:
        total += mark

    return total

print(calculate_total(80, 75, 90))
print(calculate_total(60, 10, 222))
print(calculate_total(50, 70, 60, 80))