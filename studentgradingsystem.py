# Predefined subjects
subjects = ['Math', 'English', 'Science']

# Custom exceptions
class StudentNotFoundError(Exception):
    pass

class InvalidGradeError(Exception):
    pass

# Student class to manage individual student data
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if not (0 <= grade <= 100):
            raise InvalidGradeError("Grade must be between 0 and 100.")
        self.grades[subject] = grade

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(subjects)

    def __str__(self):
        grade_details = ", ".join(f"{sub}: {grade}" for sub, grade in self.grades.items())
        return f"Student: {self.name}, Grades: [{grade_details}], Average: {self.calculate_average():.2f}"

# Gradebook class to manage the student records
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

# Main Gradebook instance
gradebook = Gradebook()

# Function to display the main menu
def display_menu():
    print("\n---- Menu ----")
    print("1. Add New Student")
    print("2. Remove a Student")
    print("3. Assign Grades to a Student")
    print("4. Update Student Grades")
    print("5. View All Students' Grades")
    print("6. Search for a Student")
    print("7. Sort Students by Name")
    print("8. Sort Students by Average Grade")
    print("9. Exit")

# Main program loop
while True:
    display_menu()
    choice = input("Select an option (1-9): ").strip()

    if choice == "1":
        student_name = input("Enter the new student's name: ").strip()
        try:
            gradebook.add_student(student_name)
        except Exception as e:
            print(e)

    elif choice == "2":
        student_name = input("Enter the name of the student to remove: ").strip()
        try:
            gradebook.remove_student(student_name)
        except StudentNotFoundError as e:
            print(e)

    elif choice == "3":
        student_name = input("Enter the name of the student to assign grades: ").strip()
        try:
            gradebook.add_grades_for_student(student_name)
        except StudentNotFoundError as e:
            print(e)

    elif choice == "4":
        student_name = input("Enter the name of the student to update grades: ").strip()
        try:
            gradebook.update_student_grade(student_name)
        except StudentNotFoundError as e:
            print(e)

    elif choice == "5":
        print("\nAll Students' Grades:")
        gradebook.display_all_students()

    elif choice == "6":
        student_name = input("Enter the student's name to search: ").strip()
        try:
            print("\nSearch Result:")
            print(gradebook.search_student(student_name))
        except StudentNotFoundError as e:
            print(e)

    elif choice == "7":
        print("\nStudents sorted by name:")
        sorted_by_name = gradebook.sort_students_by_name()
        for student in sorted_by_name:
            print(student)

    elif choice == "8":
        print("\nStudents sorted by average grade:")
        sorted_by_average = gradebook.bubble_sort_students_by_average()
        for student in sorted_by_average:
            print(student)

    elif choice == "9":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
