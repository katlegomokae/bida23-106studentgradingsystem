from student import Student

class Gradebook:
    def __init__(self):
        self.students = {}

    def add_student(self, student_name):
        if student_name not in self.students:
            self.students[student_name] = Student(student_name)
            print(f"Student '{student_name}' has been added.")
        else:
            print(f"Student '{student_name}' already exists.")

    def remove_student(self, student_name):
        if student_name in self.students:
            del self.students[student_name]
            print(f"Student '{student_name}' has been removed.")
        else:
            raise StudentNotFoundError(f"No record found for '{student_name}'.")

    def add_grades_for_student(self, student_name):
        student = self.students.get(student_name)
        if student:
            print(f"Entering grades for {student_name}.")
            for subject in subjects:
                student.grades[subject] = self.get_valid_grade(student_name, subject)
            print(f"Grades for {student_name} have been recorded.")
        else:
            raise StudentNotFoundError(f"No record found for '{student_name}'.")

    def get_valid_grade(self, student_name, subject):
        while True:
            try:
                grade = float(input(f"Enter {student_name}'s grade for {subject} (0-100): "))
                if 0 <= grade <= 100:
                    return grade
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")

    def update_student_grade(self, student_name):
        student = self.students.get(student_name)
        if student:
            print(f"Current grades for {student_name}: {student.grades}")
            print("Select the subject to update:")
            for idx, subject in enumerate(subjects):
                print(f"{idx + 1}. {subject}")
            try:
                subject_choice = int(input("Enter the subject number: "))
                if 1 <= subject_choice <= len(subjects):
                    selected_subject = subjects[subject_choice - 1]
                    new_grade = self.get_valid_grade(student_name, selected_subject)
                    student.grades[selected_subject] = new_grade
                    print(f"Updated {student_name}'s grade for {selected_subject}.")
                else:
                    print("Invalid subject choice.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            raise StudentNotFoundError(f"No record found for '{student_name}'.")

    def search_student(self, student_name):
        student = self.students.get(student_name)
        if student:
            return str(student)
        else:
            raise StudentNotFoundError(f"No record found for '{student_name}'.")

    def sort_students_by_name(self):
        return sorted(self.students.values(), key=lambda s: s.name)

    def bubble_sort_students_by_average(self):
        sorted_list = list(self.students.values())
        n = len(sorted_list)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if sorted_list[j].calculate_average() < sorted_list[j + 1].calculate_average():
                    sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
        return sorted_list

    def display_all_students(self):
        for student in self.students.values():
            print(student)
