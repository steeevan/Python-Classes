import json

class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = {}  # Format: {class_name: grade}
        self.classes = []  # List of enrolled classes

    def add_class(self, class_name):
        if class_name not in self.classes:
            self.classes.append(class_name)
            print(f"{class_name} added for {self.name}.")
        else:
            print(f"{class_name} is already enrolled.")

    def add_grade(self, class_name, grade):
        if class_name in self.classes:
            self.grades[class_name] = grade
            print(f"Grade {grade} added for {class_name}.")
        else:
            print(f"{class_name} is not in the enrolled classes.")

    def get_gpa(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Classes: {', '.join(self.classes) if self.classes else 'None'}")
        print(f"GPA: {self.get_gpa():.2f}")



class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, age, student_id):
        if student_id not in self.students:
            self.students[student_id] = Student(name, age, student_id)
            print(f"Student {name} added.")
        else:
            print(f"Student ID {student_id} already exists.")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student ID {student_id} removed.")
        else:
            print(f"Student ID {student_id} not found.")

    def view_student(self, student_id):
        if student_id in self.students:
            self.students[student_id].display_info()
        else:
            print(f"Student ID {student_id} not found.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump({sid: vars(stu) for sid, stu in self.students.items()}, file)
        print("Data saved successfully.")

    def load_from_file(self, filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            for sid, stu_data in data.items():
                student = Student(
                    stu_data['name'],
                    stu_data['age'],
                    stu_data['student_id']
                )
                student.classes = stu_data['classes']
                student.grades = stu_data['grades']
                self.students[sid] = student
        print("Data loaded successfully.")
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty system.")



def main():
    system = StudentManagementSystem()

    # Load existing data
    system.load_from_file("students.json")

    # Add students
    system.add_student("Alice", 20, "S001")
    system.add_student("Bob", 22, "S002")

    # Add classes and grades
    system.students["S001"].add_class("Math")
    system.students["S001"].add_grade("Math", 95)
    system.students["S002"].add_class("Physics")
    system.students["S002"].add_grade("Physics", 85)

    # View student info
    system.view_student("S001")

    # Save data
    system.save_to_file("students.json")

if __name__ == "__main__":
    main()
