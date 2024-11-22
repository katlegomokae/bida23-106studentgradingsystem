from gradebook import Gradebook

def display_menu():
    print("\n-- Menu --")
    print("1. Add New Student")
    print("2. Remove a Student")
    print("3. Assign Grades to a Student")
    print("4. Update Student Grades")
    print("5. View All Students' Grades")
    print("6. Search for a Student")
    print("7. Sort Students By Name")
    print("8. Sort Students By Average Grade")
    print("9. Exit")

def run_program():
    gradebook = Gradebook()

    while True:
        display_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            student_name = input("Enter the new student's name: ").strip()
            gradebook.add_student(student_name)
            print(f"Student '{student_name}' has been added.")

        elif choice == "2":
            student_name = input("Enter the name of the student to remove: ").strip()
            gradebook.remove_student(student_name)
            print(f"Student '{student_name}' has been removed.")

        elif choice == "3":
            student_name = input("Enter the name of the student to assign grades: ").strip()
            subject = input("Enter the subject: ").strip()
            grade = float(input(f"Enter {student_name}'s grade for {subject} (0-100): ").strip())
            gradebook.add_grades_for_student(student_name, subject, grade)

        elif choice == "4":
            student_name = input("Enter the name of the student to update grades: ").strip()
            subject = input("Enter the subject to update: ").strip()
            new_grade = float(input(f"Enter new grade for {subject}: ").strip())
            gradebook.update_student_grade(student_name, subject, new_grade)

        elif choice == "5":
            print("\nAll Students' Grades:")
            gradebook.display_all_students()

        elif choice == "6":
            student_name = input("Enter the student's name to search: ").strip()
            print(gradebook.search_student(student_name))

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

if __name__ == "__main__":
    run_program()
