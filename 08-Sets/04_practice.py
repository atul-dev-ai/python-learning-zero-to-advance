# ==========================================
# Practice - Sets
# ==========================================

# --- Practice 1: Unique Emails ---
emails = [
    "atul@gmail.com",
    "Rahim@gmail.com",
    "atul@gmail.com",
    "karim@gmail.com",
    "sakib@gmail.com"
]
print(type(emails)) # list

unique_emails = set(emails)
print(unique_emails)
print(type(unique_emails)) # set


# --- Practice 2: Common Subjects ---
student_a = {"Math", "Physics", "Python"}
student_b = {"Python", "English", "Math"}

common_subjects = student_a & student_b
print(common_subjects)


# --- Add your new practice problems below ---
