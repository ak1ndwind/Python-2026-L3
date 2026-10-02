import numpy as np
from domains import StudentMark
import input as in_mod
import output as out_mod


class AppCoordinator:
    """Coordinates system state, inputs, outputs, and math calculations."""

    def __init__(self):
        self.students = []  # List of Student objects
        self.courses = []   # List of Course objects
        self.marks = {}     # Dict: (course_id, student_id) -> StudentMark

    # --- Student Coordination ---
    def add_students(self):
        count = in_mod.input_number_of_students()
        for i in range(count):
            print(f"\n--- Adding Student {i + 1}/{count} ---")
            student = in_mod.input_student_data()
            self.students.append(student)
        print(f"\n[+] Successfully added {count} student(s).")

    # --- Course Coordination ---
    def add_courses(self):
        count = in_mod.input_number_of_courses()
        for i in range(count):
            print(f"\n--- Adding Course {i + 1}/{count} ---")
            course = in_mod.input_course_data()
            self.courses.append(course)
        print(f"\n[+] Successfully added {count} course(s).")

    def find_course(self, course_id: str):
        for c in self.courses:
            if c.get_id() == course_id:
                return c
        return None

    def find_student(self, student_id: str):
        for s in self.students:
            if s.get_id() == student_id:
                return s
        return None

    # --- Mark Coordination ---
    def add_marks(self):
        if not self.courses:
            print("\n[!] Please input courses before entering marks.")
            return
        if not self.students:
            print("\n[!] Please input students before entering marks.")
            return

        out_mod.display_courses(self.courses)
        course_id = input("\nEnter Course ID to input marks for: ").strip()
        course = self.find_course(course_id)

        if not course:
            print(f"[!] Course ID '{course_id}' not found.")
            return

        print(f"\nEntering marks for course: {course.get_name()} ({course_id})")
        for student in self.students:
            score = in_mod.input_student_mark(student.get_name(), student.get_id())
            mark_record = StudentMark(course_id, student.get_id(), score)
            self.marks[(course_id, student.get_id())] = mark_record

        print(f"\n[+] Marks recorded successfully for {course.get_name()}.")

    def show_marks(self):
        if not self.courses or not self.students:
            print("\n[!] Both courses and students must exist to show marks.")
            return

        out_mod.display_courses(self.courses)
        course_id = input("\nEnter Course ID to view marks: ").strip()
        course = self.find_course(course_id)

        if not course:
            print(f"[!] Course ID '{course_id}' not found.")
            return

        out_mod.display_course_marks(course, self.students, self.marks)

    # --- NumPy Weighted GPA ---
    def calculate_gpa(self, student_id: str):
        scores = []
        credits = []

        for course in self.courses:
            key = (course.get_id(), student_id)
            if key in self.marks:
                scores.append(self.marks[key].get_mark())
                credits.append(course.get_credits())

        if not scores:
            return None

        marks_array = np.array(scores, dtype=float)
        credits_array = np.array(credits, dtype=float)

        weighted_gpa = np.sum(marks_array * credits_array) / np.sum(credits_array)
        return float(weighted_gpa)

    def show_student_gpa(self):
        if not self.students:
            print("\n[!] No students available.")
            return

        out_mod.display_students(self.students)
        student_id = input("\nEnter Student ID to calculate GPA: ").strip()
        student = self.find_student(student_id)

        if not student:
            print(f"[!] Student ID '{student_id}' not found.")
            return

        gpa = self.calculate_gpa(student_id)
        out_mod.display_student_gpa(student, gpa)

    def show_ranking(self):
        if not self.students:
            print("\n[!] No students to sort.")
            return

        # Build list of tuples: (Student, GPA)
        student_gpas = [(s, self.calculate_gpa(s.get_id())) for s in self.students]
        
        # Sort descending by GPA (None sorted to bottom as -1.0)
        student_gpas.sort(
            key=lambda pair: -1.0 if pair[1] is None else pair[1],
            reverse=True
        )

        out_mod.display_gpa_ranking(student_gpas)

    # --- Coordination Loop ---
    def run(self):
        while True:
            out_mod.print_menu()
            choice = input("Enter your choice [0-8]: ").strip()

            if choice == "1":
                self.add_students()
            elif choice == "2":
                self.add_courses()
            elif choice == "3":
                self.add_marks()
            elif choice == "4":
                out_mod.display_students(self.students)
            elif choice == "5":
                out_mod.display_courses(self.courses)
            elif choice == "6":
                self.show_marks()
            elif choice == "7":
                self.show_student_gpa()
            elif choice == "8":
                self.show_ranking()
            elif choice == "0":
                print("\nExiting program. Goodbye!")
                break
            else:
                print("\n[!] Invalid choice! Please select an option between 0 and 8.")


if __name__ == "__main__":
    app = AppCoordinator()
    app.run()
