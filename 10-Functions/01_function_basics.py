# ==========================================
# 01_function_basics.py
# ==========================================

# ------------------------------------------
# 1. What is a Function?
# ------------------------------------------
# A **Function** is a reusable block of code that has a **name**. 
# We can execute that block of code anytime just by calling its name.
#
# Simply put:
# > **Function = A reusable block of code designed to perform a specific task.**
#p
# ### Real-life example:
# Think of a **washing machine** at home.
# You just press the `Start` button and the machine:
# Takes water
# ↓
# Washes clothes
# ↓
# Rinses
# ↓
# Spins
# ↓
# Done
#
# You don't have to manually do these steps every time.
# Functions in programming work the same way.
#
# Function -> A specific task -> Call it when needed.

# ------------------------------------------
# 2. What is the problem without Functions?
# ------------------------------------------
# Suppose you want to print "Hello Atul" 3 times.
# Without a function:
# print("Hello Atul")
# print("Hello Atul")
# print("Hello Atul")
#
# This works. But what if you have to do it 100 times?
# You'd have to write the same code again and again.
#
# Using a Function:
# def say_hello():
#     print("Hello Atul")
#
# Then:
# say_hello()
# say_hello()
# say_hello()
#
# The code inside the function runs as many times as you call it.

# ------------------------------------------
# 3. Syntax for Creating a Function
# ------------------------------------------
# In Python, we use the `def` keyword to create a function.
#
# def function_name():
#     # code
#
# Breakdown:
# def             -> Keyword to create a function
# function_name   -> The name of the function
# ()              -> Where we can put inputs/parameters (later)
# :               -> Marks the start of the function body
#
# Example:
# def greet():
#     print("Hello!")
#
# Now we have **created/defined** a Function.
# But it hasn't **executed/run** yet.

# ------------------------------------------
# 4. What is a Function Call?
# ------------------------------------------
# To run the code inside a function, we must **call** the function.
#
# def greet():
#     print("Hello!")
#
# greet()
#
# Output: Hello!
#
# Defining the function tells Python: "Create a function named greet."
# Calling the function (`greet()`) tells Python: "Run the code inside greet."

# ------------------------------------------
# 5. Keep this flow in mind
# ------------------------------------------
# Create Function 
#      ↓
#    def greet():
#      ↓
# Call Function
#      ↓
#    greet()
#      ↓
# Code executes

# ------------------------------------------
# 6. An Important Note
# ------------------------------------------
# Look at this code:
# def greet():
#     print("Hello!")
#
# What will be the output?
# **Nothing will happen.**
#
# Because we only **defined** the function. We didn't call it.
# Correct way:
# def greet():
#     print("Hello!")
#
# greet()  <- This triggers the output.

# ------------------------------------------
# 7. Why do we use Functions?
# ------------------------------------------
# Main advantages:
# 
# ① Code Reusability
# Write once, use many times.
#
# ② Code is shorter and cleaner
#
# ③ Easy to repeat tasks
#
# ④ Large programs are easier to manage
# You can break a large program into smaller, manageable functions.
# (e.g., add_student(), delete_student(), update_student())

# ------------------------------------------
# 8. Real Example
# ------------------------------------------
# Let's make a function to print a student's name:
#
# def student_name():
#     print("My name is Atul")
#
# Call:
# student_name()   # Output: My name is Atul
# student_name()   # Output: My name is Atul

# ------------------------------------------
# 9. Multiple Statements inside a Function
# ------------------------------------------
# def student_info():
#     print("Name: Atul")
#     print("University: DIU")
#     print("Department: SWE")
#
# student_info()
# 
# Output:
# Name: Atul
# University: DIU
# Department: SWE

# ------------------------------------------
# 10. Indentation is Crucial
# ------------------------------------------
# Code inside a function must be indented (usually 4 spaces).
#
# Correct:
# def greet():
#     print("Hello")
#     print("Welcome")
#
# Incorrect:
# def greet():
# print("Hello")  <- Raises an IndentationError!

# ------------------------------------------
# 11. Concept Summary
# ------------------------------------------
# `def`             -> Keyword to define a function
# Function name     -> The identifier of the function
# `()`              -> Place for parameters
# `:`               -> Start of function block
# Indentation       -> Identifies the function's internal code
# Function call     -> Triggers the function execution (`function_name()`)

# ------------------------------------------
# 🎯 Top 3 Important Rules
# ------------------------------------------
# 1️⃣ Create Function (def greet():)
# 2️⃣ Call Function (greet())
# 3️⃣ Reuse Function (greet() greet() greet())

# ------------------------------------------
# 📝 Practice Tasks — Do it yourself!
# ------------------------------------------
# Write your solutions below.

# ### Task 1
# Create a function named `hello()` that prints: "Hello Python"

# ### Task 2
# Create a function named `student_info()` that outputs:
# Name: Atul
# University: Daffodil International University
# Department: Software Engineering

# ### Task 3 ⭐
# Create a function named `my_routine()`.
# Inside the function, print:
# I wake up early.
# I exercise.
# I study Python.
# I go to university.
# Then, call the function **2 times**.

# ### Task 4 ⭐⭐
# Create a function: `def welcome():`
# It should output:
# Welcome to Python Programming
# Let's learn Functions
# Then, call the function **3 times**.

# ------------------------------------------
# 🔑 Today's Formula
# ------------------------------------------
# DEFINE
#   ↓
# def function_name():
#       ↓
#     CODE
#       ↓
# CALL
#   ↓
# function_name()
#
# **Remember:** Creating a function and running a function are **two different things**.
# Next, we will learn about **Parameters & Arguments**!


def introduce():
    print("my name is Atul Paul")
    print("i am a CIS Student")

introduce()