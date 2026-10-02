import math
from domains import Student, Course


def input_number_of_students() -> int:
    """Input and validate the number of students."""
    while True:
        try:
            num = int(input("Enter number of students: "))
            if num > 0:
                return num
            print("[!] Please enter a positive integer greater than 0.")
        except ValueError:
            print("[!] Invalid integer. Please try again.")


def input_student_data() -> Student:
    """Input information for a single student."""
    s_id = input("  Enter Student ID: ").strip()
    name = input("  Enter Student Name: ").strip()
    dob = input("  Enter Date of Birth (DD/MM/YYYY): ").strip()
    return Student(s_id, name, dob)


def input_number_of_courses() -> int:
    """Input and validate the number of courses."""
    while True:
        try:
            num = int(input("Enter number of courses: "))
            if num > 0:
                return num
            print("[!] Please enter a positive integer greater than 0.")
        except ValueError:
            print("[!] Invalid integer. Please try again.")


def input_course_data() -> Course:
    """Input information for a single course including credits."""
    c_id = input("  Enter Course ID: ").strip()
    name = input("  Enter Course Name: ").strip()
    while True:
        try:
            credits = int(input("  Enter Course Credits (positive integer): "))
            if credits > 0:
                return Course(c_id, name, credits)
            print("  [!] Credits must be greater than 0.")
        except ValueError:
            print("  [!] Please enter a valid integer for credits.")


def input_student_mark(student_name: str, student_id: str) -> float:
    """
    Input and round-down student score to 1-digit decimal using math.floor().
    """
    while True:
        try:
            score = float(input(f"  Enter mark for {student_name} (ID: {student_id}) [0-20]: "))
            if 0.0 <= score <= 20.0:
                # Round-down to 1 decimal place using math.floor
                floored_score = math.floor(score * 10.0) / 10.0
                return floored_score
            print("  [!] Mark must be between 0.0 and 20.0.")
        except ValueError:
            print("  [!] Please enter a valid decimal number.")
