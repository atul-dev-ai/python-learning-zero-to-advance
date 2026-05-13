"""
Docsting for operators.member
in
not in
"""

student = ['Aman', 'Chaman', 'Kara']
print("Rahul" in student)

print("Aman" in student)

print("Atul" not in student) # True



allowed_users = ['admin', 'manager', 'staff']
user = input("Enter your role: ")
print(user in allowed_users)

blocked_user = ['user1', 'user2']
user_id = input("Enter user id: ")
print(user_id not in blocked_user)

message = 'I love Python Programming'
print("Python" in message)
print('python' in message)