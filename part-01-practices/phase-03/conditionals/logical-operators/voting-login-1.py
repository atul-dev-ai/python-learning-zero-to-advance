"""
        Con1        Con2        Result

          T          T            T
          T          F            F
          F          T            F
          F          F            F
"""


age = int(input("Enter your age: "))
nationality = str(input("Enter your nationality: "))
if age >= 18 and nationality == "Bangladesh":
    print("You can vote for up coming polls")
elif age < 18 and nationality != "Bangladesh":
    print("You cannot vote in next polls");