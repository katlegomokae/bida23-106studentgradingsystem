from student import Student

class Gradebook:
    def __init__(self):
        self.students = {}

    def add_student(self, student_name):
        if student_name not in self.students:
            self.students[student_name] = Student(student_name)
        else:
            raise ValueError(f"Student {student_name} already exists.")

    def remove_student(self, student_name):
        if student_name in self.students:
            del self.students[student_name]
        else:
            raise KeyError(f"Student {student_name} not found.")

    def add_grades_for_student(self, student_name, subject, grade):
        if student_name in self.students:
            self.students[student_name].add_grade(subject, grade)
        else:
            raise KeyError(f"Student {student_name} not found.")

    def update_student_grade(self, student_name, subject, new_grade):
        if student_name in self.students:
            self.students[student_name].update_grade(subject, new_grade)
        else:
            raise KeyError(f"Student {student_name} not found.")

    def display_all_students(self):
        for student in self.students.values():
            print(student)

    def search_student(self, student_name):
        if student_name in self.students:
            return str(self.students[student_name])
        else:
            raise KeyError(f"Student {student_name} not found.")
