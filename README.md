# STUDENT GRADING SYSTEM

The Student Grading System is a Python application that helps manage student records and grades efficiently by using object-oriented programming. It allows users to add and manage students, assign grades in multiple subjects, calculate averages, and sort or search student records.

## DESCRIPTION
This project provides a streamlined solution for tracking student academic performance. Each student is represented as an object with attributes for name and subject grades. The program allows users to add students, assign or update subject-specific grades, calculate the average score, and display all student information. For enhanced user control, students can be sorted by name or average grade, with exception handling and validations to ensure data integrity.

The system includes:

-Adding and removing student records
-Assigning grades per subject with validation (grades must be 0-100)
-Viewing individual student details or all records
-Searching for specific students and sorting by name or average grade
-Custom exception handling for missing students and invalid grades

## GETTING STARTED
Before installing the program, make sure to have the following prerequisites installed;
Python 3.6 or higher and any operating system that supports Python i.e MacOS, Windows 10, Linux

## INSTALLING
CLONE or downlowad the project files from the repository:
git clone https://github.com/katlegomokae/studentgradingsystem.git
Navigate to the project directory:
cd student-grading-system

## Executing Program
To run the program:
1. Open your terminal or command prompt.
2. Navigate to the directory containing studentgradingsystem.py
3. Run the folowing command:
   python studentgradingsystem.py
4. Follow the on-screen prompts to add students, assign grades, and interact with the grading system.

## Help
Common Issues:
- StudentNotFoundError: Occurs if trying to update or delete a non-existent student.
- InvalidGradeError: Ensures grades are between 0 and 100.
Troubleshooting Steps:
- Verify student names are spelled correctly.
- Ensure grades are valid integers within specified range.

## Authors
-Katlego Angela Mokae
   - Contact Info: bida23-106@thuto.bac.ac.bw
   - GitHub: katlegomokae

## Version History
- 0.2: Added sorting functionality, exception handling improvements.
- 0.1: Initial release with basic student and grade management features

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgements
Inspired by the open-source community and resources on OOP and exception handling in Python, including:
- awesome-readme
- dbader
