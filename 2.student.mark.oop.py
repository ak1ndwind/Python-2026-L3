class Person:
    """Base class representing a general person."""

    def __init__(self, person_id: str = "", name: str = "", dob: str = ""):
        # Private attributes (encapsulation)
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
        """Input person details from console."""
        self.__id = input("  Enter ID: ").strip()
        self.__name = input("  Enter Name: ").strip()
        self.__dob = input("  Enter Date of Birth (DD/MM/YYYY): ").strip()

    def list(self):
        """Display formatted person info."""
        print(f"ID: {self.__id:<12} Name: {self.__name:<20} DoB: {self.__dob:<12}")

    def __str__(self) -> str:
        return f"Person[ID={self.__id}, Name={self.__name}, DoB={self.__dob}]"


# 2. SUBCLASS: Student (Demonstrates Inheritance & Polymorphism)

class Student(Person):
    """Student class inheriting from Person."""

    def __init__(self, student_id: str = "", name: str = "", dob: str = ""):
        # Call parent constructor using super()
        super().__init__(student_id, name, dob)

    # Polymorphic method overriding
    def input(self):
        """Prompt specifically for student information."""
        print("  --- Student Details ---")
        student_id = input("  Enter Student ID: ").strip()
        name = input("  Enter Student Name: ").strip()
        dob = input("  Enter Date of Birth (DD/MM/YYYY): ").strip()
        
        self.set_id(student_id)
        self.set_name(name)
        self.set_dob(dob)

    def list(self):
        """Display student record."""
        print(f"| {self.get_id():<12} | {self.get_name():<20} | {self.get_dob():<15} |")

    def __str__(self) -> str:
        return f"Student[ID={self.get_id()}, Name={self.get_name()}, DoB={self.get_dob()}]"


# 3. CLASS: Course (Demonstrates Polymorphism: .input(), .list())

class Course:
    """Class representing an academic course."""

    def __init__(self, course_id: str = "", name: str = ""):
        self.__id = course_id
        self.__name = name

    # --- Getters & Setters ---
    def get_id(self) -> str:
        return self.__id

    def set_id(self, course_id: str):
        self.__id = course_id

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    # Polymorphic methods
    def input(self):
        """Prompt for course information."""
        self.__id = input("  Enter Course ID: ").strip()
        self.__name = input("  Enter Course Name: ").strip()

    def list(self):
        """Display course record."""
        print(f"| {self.get_id():<12} | {self.get_name():<25} |")

    def __str__(self) -> str:
        return f"Course[ID={self.__id}, Name={self.__name}]"


# 4. CLASS: StudentMark (Encapsulates Mark Association)

class StudentMark:
    """Class encapsulating a student's grade in a course."""

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
        return f"StudentMark(Course={self.__course_id}, Student={self.__student_id}, Mark={self.__mark:.2f})"

# 5. SYSTEM MANAGER: StudentMarkManagement

class StudentMarkManagement:
    """Coordinates student, course, and mark management operations."""

    def __init__(self):
        self.__students = []  # List of Student objects
        self.__courses = []   # List of Course objects
        self.__marks = {}     # Dict: (course_id, student_id) -> StudentMark object

    # --- Student Operations ---
    def input_number_of_students(self) -> int:
        """Prompt and validate student count."""
        while True:
            try:
                num = int(input("Enter number of students to add: "))
                if num <= 0:
                    print("[!] Please enter a positive integer greater than 0.")
                    continue
                return num
            except ValueError:
                print("[!] Invalid integer. Please try again.")

    def input_students(self):
        """Batch input students using polymorphic Student.input()."""
        count = self.input_number_of_students()
        for i in range(count):
            print(f"\n--- Adding Student {i + 1}/{count} ---")
            student = Student()
            student.input()  # Polymorphic call
            self.__students.append(student)
        print(f"\n[+] Successfully added {count} student(s).")

    def list_students(self):
        """List all students."""
        if not self.__students:
            print("\n[!] No students registered yet.")
            return

        print("\n" + "=" * 58)
        print(f"| {'Student ID':<12} | {'Student Name':<20} | {'DoB':<15} |")
        print("-" * 58)
        for student in self.__students:
            student.list()  # Polymorphic call
        print("=" * 58)

    # --- Course Operations ---
    def input_number_of_courses(self) -> int:
        """Prompt and validate course count."""
        while True:
            try:
                num = int(input("Enter number of courses to add: "))
                if num <= 0:
                    print("[!] Please enter a positive integer greater than 0.")
                    continue
                return num
            except ValueError:
                print("[!] Invalid integer. Please try again.")

    def input_courses(self):
        """Batch input courses using polymorphic Course.input()."""
        count = self.input_number_of_courses()
        for i in range(count):
            print(f"\n--- Adding Course {i + 1}/{count} ---")
            course = Course()
            course.input()  # Polymorphic call
            self.__courses.append(course)
        print(f"\n[+] Successfully added {count} course(s).")

    def list_courses(self):
        """List all courses."""
        if not self.__courses:
            print("\n[!] No courses available.")
            return

        print("\n" + "=" * 45)
        print(f"| {'Course ID':<12} | {'Course Name':<25} |")
        print("-" * 45)
        for course in self.__courses:
            course.list()  # Polymorphic call
        print("=" * 45)

    # --- Mark Operations ---
    def find_course(self, course_id: str):
        """Find course by ID."""
        for c in self.__courses:
            if c.get_id() == course_id:
                return c
        return None

    def input_marks_for_course(self):
        """Select a course and enter marks for all students."""
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
            print(f"[!] Course with ID '{course_id}' was not found.")
            return

        print(f"\nEntering marks for: {course.get_name()} ({course.get_id()})")
        for student in self.__students:
            while True:
                try:
                    score = float(input(f"  Enter mark for {student.get_name()} (ID: {student.get_id()}) [0-20]: "))
                    if 0.0 <= score <= 20.0:
                        mark_record = StudentMark(course_id, student.get_id(), score)
                        self.__marks[(course_id, student.get_id())] = mark_record
                        break
                    else:
                        print("  [!] Mark must be between 0 and 20.")
                except ValueError:
                    print("  [!] Invalid number. Please enter a valid float or int.")

        print(f"\n[+] Marks recorded successfully for course '{course.get_name()}'.")

    def show_student_marks(self):
        """Show marks of all students for a selected course."""
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
            print(f"[!] Course with ID '{course_id}' was not found.")
            return

        print("\n" + "=" * 55)
        print(f"Course: {course.get_name()} ({course.get_id()})")
        print("-" * 55)
        print(f"| {'Student ID':<12} | {'Student Name':<20} | {'Mark':<8} |")
        print("-" * 55)

        for student in self.__students:
            key = (course_id, student.get_id())
            if key in self.__marks:
                mark_val = f"{self.__marks[key].get_mark():.2f}"
            else:
                mark_val = "N/A"
            print(f"| {student.get_id():<12} | {student.get_name():<20} | {mark_val:<8} |")

        print("=" * 55)

    # --- Menu Loop ---

    def run(self):
        """Run the interactive console menu."""
        while True:
            print("\n" + "=" * 45)
            print("   STUDENT MARK MANAGEMENT (OOP SYSTEM)")
            print("=" * 45)
            print("1. Input students")
            print("2. Input courses")
            print("3. Input marks for a course")
            print("4. List students")
            print("5. List courses")
            print("6. Show student marks for a course")
            print("0. Exit")
            print("=" * 45)

            choice = input("Enter your choice [0-6]: ").strip()

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
            elif choice == "0":
                print("\nExiting program. Goodbye!")
                break
            else:
                print("\n[!] Invalid choice! Please select an option between 0 and 6.")

# ENTRY POINT

if __name__ == "__main__":
    system = StudentMarkManagement()
    system.run()