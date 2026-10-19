
from student import Student
from manager import StudentManager


manager = StudentManager()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ").strip()
        student_id = input("Enter student ID: ").strip()

        try:
            marks_text = input(
                "Enter marks separated by commas: "
            )
            marks = [
                float(mark.strip())
                for mark in marks_text.split(",")
            ]

            if not name or not student_id:
                print("Name and student ID cannot be empty.")
                continue

            student = Student(name, student_id, marks)
            manager.add_student(student)

        except (ValueError, TypeError) as error:
            print("Invalid input:", error)

    elif choice == "2":
        manager.show_all_students()

    elif choice == "3":
        student_id = input("Enter student ID: ").strip()
        student = manager.find_student(student_id)

        if student:
            student.show_info()
        else:
            print("Student not found.")

    elif choice == "4":
        print("Program closed.")
        break

    else:
        print("Invalid choice. Try again.")
