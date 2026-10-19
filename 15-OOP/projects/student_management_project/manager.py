
import json
from pathlib import Path
from student import Student


class StudentManager:
    
    def __init__(self, filename="students.json"):
        self.filename = Path(__file__).with_name(filename)
        self.students = []
        self.load_data()


    def add_student(self, student):
        for existing in self.students:
            if existing.student_id == student.student_id:
                print("Student ID already exists!")
                return

        self.students.append(student)
        self.save_data()
        print("Student added successfully!")

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    def show_all_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            print("-" * 30)
            student.show_info()

    def save_data(self):
        data = [student.to_dict() for student in self.students]

        with self.filename.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def load_data(self):
        if not self.filename.exists():
            return

        try:
            with self.filename.open("r", encoding="utf-8") as file:
                data = json.load(file)

            self.students = [
                Student.from_dict(item) for item in data
            ]

        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            print("Could not load student data:", error)
            self.students = []
