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
