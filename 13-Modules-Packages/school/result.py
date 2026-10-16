def calculate_total(marks):
    return sum(marks)

def calculate_avg(marks):
    if len(marks) == 0:
        return 0
    
    return sum(marks) / len(marks)

def get_result(avg):
    if avg >= 40:
        return "Pass"
    else:
        return "Fail"