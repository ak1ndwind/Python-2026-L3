import math
import numpy as np

# 1. BASE CLASS: Person

class Person:
    """Base class representing a person with encapsulated attributes."""

    def __init__(self, person_id: str = "", name: str = "", dob: str = ""):
        self.__id = person_id
        self.__name = name
        self.__dob = dob

    # --- Getters & Setters ---
    def get_id(self) -> str:
        return self.__id

    def set_id(self, person_id: str):
        self.__id = person_id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_dob(self) -> str:
        return self.__dob

    def set_dob(self, dob: str):
        self.__dob = dob

    # --- Polymorphic Methods ---
    def input(self):
        """Input person details."""
        self.__id = input("  Enter ID: ").strip()
        self.__name = input("  Enter Name: ").strip()
        self.__dob = input("  Enter Date of Birth (DD/MM/YYYY): ").strip()

    def list(self):
        """Display person details."""
        print(f"| {self.__id:<12} | {self.__name:<20} | {self.__dob:<15} |")

    def __str__(self) -> str:
        return f"Person[ID={self.__id}, Name={self.__name}, DoB={self.__dob}]"

# 2. SUBCLASS: Student

class Student(Person):
    """Student class inheriting from Person."""

    def __init__(self, student_id: str = "", name: str = "", dob: str = ""):
        super().__init__(student_id, name, dob)

    def input(self):
        """Polymorphic input method for Student."""
        print("  --- Student Details ---")
        student_id = input("  Enter Student ID: ").strip()
        name = input("  Enter Student Name: ").strip()
        dob = input("  Enter Date of Birth (DD/MM/YYYY): ").strip()

        self.set_id(student_id)
        self.set_name(name)
        self.set_dob(dob)

    def list(self):
        """Polymorphic list method for Student."""
        print(f"| {self.get_id():<12} | {self.get_name():<20} | {self.get_dob():<15} |")

    def __str__(self) -> str:
        return f"Student[ID={self.get_id()}, Name={self.get_name()}, DoB={self.get_dob()}]"

# 3. CLASS: Course (With Credits)

class Course:
    """Represents a course with ID, Name, and Credit count."""

    def __init__(self, course_id: str = "", name: str = "", credits: int = 1):
        self.__id = course_id
        self.__name = name
        self.__credits = credits

    # --- Getters & Setters ---
    def get_id(self) -> str:
        return self.__id

    def set_id(self, course_id: str):
        self.__id = course_id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_credits(self) -> int:
        return self.__credits

    def set_credits(self, credits: int):
        if credits > 0:
            self.__credits = credits
        else:
            raise ValueError("Credits must be a positive integer.")

    # --- Polymorphic Methods ---
    def input(self):
        """Prompt for course info including credits."""
        print("  --- Course Details ---")
        self.__id = input("  Enter Course ID: ").strip()
        self.__name = input("  Enter Course Name: ").strip()
        while True:
            try:
                c = int(input("  Enter Course Credits (e.g., 1, 2, 3, 4): "))
                if c > 0:
                    self.__credits = c
                    break
                print("  [!] Credits must be a positive integer.")
            except ValueError:
                print("  [!] Please enter a valid integer for credits.")

    def list(self):
        """Display course information."""
        print(f"| {self.get_id():<12} | {self.get_name():<25} | {self.get_credits():<8} |")

    def __str__(self) -> str:
        return f"Course[ID={self.__id}, Name={self.__name}, Credits={self.__credits}]"

# 4. CLASS: StudentMark

class StudentMark:
    """Encapsulates course ID, student ID, and mark."""

    def __init__(self, course_id: str, student_id: str, mark: float):
        self.__course_id = course_id
        self.__student_id = student_id
        self.__mark = mark

    def get_course_id(self) -> str:
        return self.__course_id

    def get_student_id(self) -> str:
        return self.__student_id

    def get_mark(self) -> float:
        return self.__mark

    def set_mark(self, mark: float):
        if 0.0 <= mark <= 20.0:
            self.__mark = mark
        else:
            raise ValueError("Mark must be between 0.0 and 20.0")

    def __str__(self) -> str:
        return f"StudentMark(Course={self.__course_id}, Student={self.__student_id}, Mark={self.__mark:.1f})"

# 5. SYSTEM MANAGER: StudentMarkManagement

class StudentMarkManagement:
    """Manages students, courses, marks, and GPA calculations."""

    def __init__(self):
        self.__students = []  # List of Student objects
        self.__courses = []   # List of Course objects
        self.__marks = {}     # Dict: (course_id, student_id) -> StudentMark object

    # --- Student Operations ---
    def input_number_of_students(self) -> int:
        while True:
            try:
                num = int(input("Enter number of students: "))
                if num > 0:
                    return num
                print("[!] Number must be greater than 0.")
            except ValueError:
                print("[!] Please enter an integer.")

    def input_students(self):
        count = self.input_number_of_students()
        for i in range(count):
            print(f"\n--- Adding Student {i + 1}/{count} ---")
            student = Student()
            student.input()
            self.__students.append(student)
        print(f"\n[+] Successfully added {count} student(s).")

    def list_students(self):
        if not self.__students:
            print("\n[!] No students registered yet.")
            return

        print("\n" + "=" * 58)
        print(f"| {'Student ID':<12} | {'Student Name':<20} | {'DoB':<15} |")
        print("-" * 58)
        for student in self.__students:
            student.list()
        print("=" * 58)

    # --- Course Operations ---
    def input_number_of_courses(self) -> int:
        while True:
            try:
                num = int(input("Enter number of courses: "))
                if num > 0:
                    return num
                print("[!] Number must be greater than 0.")
            except ValueError:
                print("[!] Please enter an integer.")

    def input_courses(self):
        count = self.input_number_of_courses()
        for i in range(count):
            print(f"\n--- Adding Course {i + 1}/{count} ---")
            course = Course()
            course.input()
            self.__courses.append(course)
        print(f"\n[+] Successfully added {count} course(s).")

    def list_courses(self):
        if not self.__courses:
            print("\n[!] No courses available.")
            return

        print("\n" + "=" * 54)
        print(f"| {'Course ID':<12} | {'Course Name':<25} | {'Credits':<8} |")
        print("-" * 54)
        for course in self.__courses:
            course.list()
        print("=" * 54)

    def find_course(self, course_id: str):
        for c in self.__courses:
            if c.get_id() == course_id:
                return c
        return None

    def find_student(self, student_id: str):
        for s in self.__students:
            if s.get_id() == student_id:
                return s
        return None

    # --- Mark Operations with math.floor() ---
    def input_marks_for_course(self):
        """Input marks and round down to 1-digit decimal using math.floor()."""
        if not self.__courses:
            print("\n[!] Please input courses before entering marks.")
            return
        if not self.__students:
            print("\n[!] Please input students before entering marks.")
            return

        self.list_courses()
        course_id = input("\nEnter Course ID to input marks for: ").strip()
        course = self.find_course(course_id)

        if not course:
            print(f"[!] Course ID '{course_id}' not found.")
            return

        print(f"\nEntering marks for course: {course.get_name()} ({course_id})")
        for student in self.__students:
            while True:
                try:
                    raw_score = float(input(f"  Enter mark for {student.get_name()} (ID: {student.get_id()}) [0-20]: "))
                    if 0.0 <= raw_score <= 20.0:
                        # Use math.floor to round down to 1 decimal place
                        floored_score = math.floor(raw_score * 10.0) / 10.0
                        mark_record = StudentMark(course_id, student.get_id(), floored_score)
                        self.__marks[(course_id, student.get_id())] = mark_record
                        print(f"    -> Recorded mark (floored to 1-decimal): {floored_score:.1f}")
                        break
                    else:
                        print("  [!] Mark must be between 0.0 and 20.0.")
                except ValueError:
                    print("  [!] Please enter a valid numerical value.")

        print(f"\n[+] Marks recorded successfully for {course.get_name()}.")

    def show_student_marks(self):
        if not self.__courses:
            print("\n[!] No courses available.")
            return
        if not self.__students:
            print("\n[!] No students available.")
            return

        self.list_courses()
        course_id = input("\nEnter Course ID to view marks: ").strip()
        course = self.find_course(course_id)

        if not course:
            print(f"[!] Course ID '{course_id}' not found.")
            return

        print("\n" + "=" * 55)
        print(f"Marks for Course: {course.get_name()} ({course.get_id()})")
        print("-" * 55)
        print(f"| {'Student ID':<12} | {'Student Name':<20} | {'Mark':<8} |")
        print("-" * 55)
        for student in self.__students:
            key = (course_id, student.get_id())
            if key in self.__marks:
                mark_str = f"{self.__marks[key].get_mark():.1f}"
            else:
                mark_str = "N/A"
            print(f"| {student.get_id():<12} | {student.get_name():<20} | {mark_str:<8} |")
        print("=" * 55)

    # --- NumPy Weighted GPA Calculation ---
    def calculate_gpa(self, student_id: str):
        """
        Calculate weighted average GPA for a given student using numpy arrays.
        Weighted GPA = sum(marks * credits) / sum(credits)
        """
        scores = []
        credits = []

        for course in self.__courses:
            key = (course.get_id(), student_id)
            if key in self.__marks:
                scores.append(self.__marks[key].get_mark())
                credits.append(course.get_credits())

        if not scores:
            return None  # No marks recorded yet

        # Convert to numpy arrays
        marks_array = np.array(scores, dtype=float)
        credits_array = np.array(credits, dtype=float)

        # Weighted sum: sum(marks * credits) / sum(credits)
        weighted_gpa = np.sum(marks_array * credits_array) / np.sum(credits_array)
        return float(weighted_gpa)

    def show_gpa_for_student(self):
        """Prompt for a student ID and display their weighted GPA."""
        if not self.__students:
            print("\n[!] No students available.")
            return

        self.list_students()
        student_id = input("\nEnter Student ID to calculate GPA: ").strip()
        student = self.find_student(student_id)

        if not student:
            print(f"[!] Student ID '{student_id}' not found.")
            return

        gpa = self.calculate_gpa(student_id)
        if gpa is None:
            print(f"\n[!] Student {student.get_name()} has no recorded marks.")
        else:
            print(f"\n[+] Weighted GPA for {student.get_name()} (ID: {student_id}): {gpa:.2f} / 20.0")

    # --- Sort Students by GPA Descending ---
    def sort_students_by_gpa(self):
        """Sort the student list by GPA descending and display the ranking."""
        if not self.__students:
            print("\n[!] No students to sort.")
            return

        # Sort in-place using Python's sort with GPA (treat None as -1 so they appear at bottom)
        self.__students.sort(
            key=lambda s: -1.0 if self.calculate_gpa(s.get_id()) is None else self.calculate_gpa(s.get_id()),
            reverse=True
        )

        print("\n" + "=" * 68)
        print("          STUDENT RANKING BY GPA (DESCENDING)")
        print("=" * 68)
        print(f"| {'Rank':<5} | {'Student ID':<12} | {'Student Name':<20} | {'GPA':<10} |")
        print("-" * 68)
        for rank, student in enumerate(self.__students, start=1):
            gpa = self.calculate_gpa(student.get_id())
            gpa_str = f"{gpa:.2f}" if gpa is not None else "N/A"
            print(f"| {rank:<5} | {student.get_id():<12} | {student.get_name():<20} | {gpa_str:<10} |")
        print("=" * 68)

    # --- Main Menu ---
    def run(self):
        while True:
            print("\n" + "=" * 50)
            print("  STUDENT MARK & GPA SYSTEM (MATH & OOP)")
            print("=" * 50)
            print("1. Input students")
            print("2. Input courses (with credits)")
            print("3. Input marks for a course (floored to 1 decimal)")
            print("4. List students")
            print("5. List courses")
            print("6. Show marks for a course")
            print("7. Calculate GPA for a student (NumPy)")
            print("8. Sort and display students by GPA descending")
            print("0. Exit")
            print("=" * 50)

            choice = input("Enter your choice [0-8]: ").strip()

            if choice == "1":
                self.input_students()
            elif choice == "2":
                self.input_courses()
            elif choice == "3":
                self.input_marks_for_course()
            elif choice == "4":
                self.list_students()
            elif choice == "5":
                self.list_courses()
            elif choice == "6":
                self.show_student_marks()
            elif choice == "7":
                self.show_gpa_for_student()
            elif choice == "8":
                self.sort_students_by_gpa()
            elif choice == "0":
                print("\nExiting program. Goodbye!")
                break
            else:
                print("\n[!] Invalid option. Please enter a number between 0 and 8.")

# ENTRY POINT

if __name__ == "__main__":
    app = StudentMarkManagement()
    app.run()