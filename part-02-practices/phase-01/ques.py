def check_result(marks):
    if marks >= 33:
        return "Pass"
    else:
        return "Fail"
    
marks = int(input("Enter your marks: "))
result = check_result(marks)
print(result)