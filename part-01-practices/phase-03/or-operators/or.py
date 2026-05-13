"""
    Con1    Con2    Result
     T        T        T
     T        F        T
     F        T        T
     F        F        F
"""

print((10 > 3) or (3 < 0))

marks = int(input("Enter marks: "))
print(marks >= 33, "Your r pass")
print(marks >= 33 or marks >= 35)