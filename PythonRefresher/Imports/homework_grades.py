"""
- Modules get used all the time throughout programming
- It helps with creating more files, with unique purposes, to help with clean maintainable code.
"""
from grade_average_service import calculate_homework

homework_assignment_grades = {
    "homework_1": 85,
    "homework_2": 100,
    "homework_3": 81
}

calculate_homework(homework_assignment_grades)
