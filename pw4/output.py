def print_menu():
    """Display main coordination menu."""
    print("\n" + "=" * 52)
    print("      STUDENT MARK MANAGEMENT SYSTEM (PW4)")
    print("=" * 52)
    print(" 1. Input students")
    print(" 2. Input courses (with credits)")
    print(" 3. Input marks for a course (floored to 1 decimal)")
    print(" 4. List students")
    print(" 5. List courses")
    print(" 6. Show marks for a course")
    print(" 7. Calculate GPA for a student (NumPy)")
    print(" 8. Sort and display students by GPA descending")
    print(" 0. Exit")
    print("=" * 52)


def display_students(students):
    """Display table of all students."""
    if not students:
        print("\n[!] No students registered yet.")
        return

    print("\n" + "=" * 58)
    print(f"| {'Student ID':<12} | {'Student Name':<20} | {'DoB':<15} |")
    print("-" * 58)
    for student in students:
        print(f"| {student.get_id():<12} | {student.get_name():<20} | {student.get_dob():<15} |")
    print("=" * 58)


def display_courses(courses):
    """Display table of all courses."""
    if not courses:
        print("\n[!] No courses available.")
        return

    print("\n" + "=" * 54)
    print(f"| {'Course ID':<12} | {'Course Name':<25} | {'Credits':<8} |")
    print("-" * 54)
    for course in courses:
        print(f"| {course.get_id():<12} | {course.get_name():<25} | {course.get_credits():<8} |")
    print("=" * 54)


def display_course_marks(course, students, marks):
    """Display marks of all students for a selected course."""
    print("\n" + "=" * 55)
    print(f"Course: {course.get_name()} ({course.get_id()})")
    print("-" * 55)
    print(f"| {'Student ID':<12} | {'Student Name':<20} | {'Mark':<8} |")
    print("-" * 55)
    for student in students:
        key = (course.get_id(), student.get_id())
        mark_val = f"{marks[key].get_mark():.1f}" if key in marks else "N/A"
        print(f"| {student.get_id():<12} | {student.get_name():<20} | {mark_val:<8} |")
    print("=" * 55)


def display_student_gpa(student, gpa):
    """Display calculated GPA for a single student."""
    if gpa is None:
        print(f"\n[!] Student {student.get_name()} has no recorded marks.")
    else:
        print(f"\n[+] Weighted GPA for {student.get_name()} (ID: {student.get_id()}): {gpa:.2f} / 20.0")


def display_gpa_ranking(ranked_students_with_gpa):
    """Display table of students ranked by GPA descending."""
    if not ranked_students_with_gpa:
        print("\n[!] No students to display in ranking.")
        return

    print("\n" + "=" * 68)
    print("          STUDENT RANKING BY GPA (DESCENDING)")
    print("=" * 68)
    print(f"| {'Rank':<5} | {'Student ID':<12} | {'Student Name':<20} | {'GPA':<10} |")
    print("-" * 68)
    for rank, (student, gpa) in enumerate(ranked_students_with_gpa, start=1):
        gpa_str = f"{gpa:.2f}" if gpa is not None else "N/A"
        print(f"| {rank:<5} | {student.get_id():<12} | {student.get_name():<20} | {gpa_str:<10} |")
    print("=" * 68)
