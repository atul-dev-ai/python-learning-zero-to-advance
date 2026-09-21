# =====================================================================
# 🚀 PYTHON FUNDAMENTALS - LEARNING NOTES
# =====================================================================
# Python is a popular, high-level, interpreted programming language.
# It is known for its simplicity and readability.

# ---------------------------------------------------------------------
# 1. VARIABLES & DATA TYPES
# ---------------------------------------------------------------------
# Variables are used to store data in memory. Python is dynamically typed,
# meaning you don't have to declare the type of a variable.

# Strings (Text)
name = "Atul"            

# Integer (Whole Numbers)
age = 20                 

# Float (Decimal Numbers)
height = 5.8             

# Boolean (True/False)
is_student = True        

# How to check the data type:
print(type(name))   # Output: <class 'str'>
print(type(age))    # Output: <class 'int'>

# ---------------------------------------------------------------------
# 2. INPUT & OUTPUT
# ---------------------------------------------------------------------
# The print() function displays output to the screen.
print("Hello, Python Learning Journey!")

# The input() function takes input from the user. It always takes input as a String.
# example_name = input("Enter your name: ")
# print("Welcome,", example_name)

# ---------------------------------------------------------------------
# 3. TYPE CONVERSION (Casting)
# ---------------------------------------------------------------------
# Sometimes you need to convert one data type to another (e.g., str to int).

num_str = "100"
num_int = int(num_str)       # Convert string to integer
num_float = float(num_int)   # Convert integer to float
num_bool = bool(1)           # 1 becomes True, 0 becomes False

# print(num_str + 50)  # Error! Cannot add str and int directly
print(num_int + 50)    # Success! Output: 150

# ---------------------------------------------------------------------
# 4. STRING FORMATTING (f-Strings)
# ---------------------------------------------------------------------
# F-strings (added in Python 3.6) are the best and easiest way to format strings.

course = "Python"
goal = "AI/ML Engineer"
print(f"I am learning {course} to become an {goal}.")

# ---------------------------------------------------------------------
# 5. COMMENTS & INDENTATION
# ---------------------------------------------------------------------
# Comments help explain the code to yourself or others. Python ignores them.

# Use the '#' symbol for single-line comments.

'''
This is a multi-line comment (also called Docstrings when used in functions).
It can span multiple lines!
'''

# Indentation (spaces at the beginning of a code line) is VERY important in Python.
# It is used to define a block of code (like inside functions or conditionals).

if age >= 18:
    print("You are an adult.") # The 4 spaces before print are MANDATORY!

# =====================================================================
# Happy Coding! Practice these concepts by writing your own code.
# =====================================================================
