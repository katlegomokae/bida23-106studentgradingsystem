class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if 0 <= grade <= 100:
            self.grades[subject] = grade
        else:
            raise ValueError("Grade must be between 0 and 100.")

    def update_grade(self, subject, new_grade):
        if subject in self.grades:
            if 0 <= new_grade <= 100:
                self.grades[subject] = new_grade
            else:
                raise ValueError("Grade must be between 0 and 100.")
        else:
            raise KeyError(f"No grade found for {subject}")

    def get_average(self):
        return sum(self.grades.values()) / len(self.grades) if self.grades else 0

    def __str__(self):
        return f"Student: {self.name}, Grades: {self.grades}, Average: {self.get_average()}"
