'''
The "x" mode creates a new file exclusively.
If the file already exists, Python raises a FileExistsError.
'''
with open("/home/atul/Documents/python-learning-zero-to-advance/11-File-Handling/new_exists.txt", "x") as file:
    file.write("name: Atul Paul\n")
print("File added successfully.")
# first time run korle file create korbe, ekoi code abar run korle file age thekei thakay error dibe.

'''
The "r+" mode always allows both reading and writng
in an existing file. It does not trucate the file automatically,
but writing can overwrite existing characters at the current position.
'''
with open("/home/atul/Documents/python-learning-zero-to-advance/11-File-Handling/new_exists.txt", "r+") as file:
    content = file.read()
    print("Old Content:", content)
    file.seek(0)
    file.write("Python")


FILE_NAME = "/home/atul/Documents/python-learning-zero-to-advance/11-File-Handling/students.txt"

def add_student():
    name = input("Enter student name: ")

    with open(FILE_NAME, "a") as file:
        file.write(name + "\n")

    print("Student added successfully")

def show_student():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()
        if len(students == 0):
            print("No students found.")
        else:
            print("\nStudent list:")

            for index, student in enumerate(students, start = 1):
                print(f"{index}. {student.strip()}")

    except FileNotFoundError:
        print("No student file found yet.")

while True:
    print("\n--- Student Record System ---")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_student()
    elif choice == "3":
        print("Program Closed")
        break
    else:
        print("Invalid Choice. Please Try again.")
    