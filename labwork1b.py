# ------------------ Input Functions ------------------

def input_number_of_students():
    """Input number of students in a class."""
    while True:
        try:
            count = int(input("Enter number of students in the class: "))
            if count > 0:
                return count
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def input_student_info():
    """Input student information: id, name, DoB and return as a dictionary."""
    print("\n--- Input Student Details ---")
    s_id = input("Enter Student ID: ").strip()
    s_name = input("Enter Student Name: ").strip()
    s_dob = input("Enter Student Date of Birth (DoB): ").strip()
    return {"id": s_id, "name": s_name, "dob": s_dob}


def input_students():
    """Populate the students list."""
    count = input_number_of_students()
    for i in range(count):
        print(f"\nStudent {i + 1}/{count}:")
        student = input_student_info()
        students.append(student)


def input_number_of_courses():
    """Input number of courses."""
    while True:
        try:
            count = int(input("Enter number of courses: "))
            if count > 0:
                return count
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def input_course_info():
    """Input course information: id, name and return as a dictionary."""
    print("\n--- Input Course Details ---")
    c_id = input("Enter Course ID: ").strip()
    c_name = input("Enter Course Name: ").strip()
    return {"id": c_id, "name": c_name}


def input_courses():
    """Populate the courses list."""
    count = input_number_of_courses()
    for i in range(count):
        print(f"\nCourse {i + 1}/{count}:")
        course = input_course_info()
        courses.append(course)


def input_marks_for_course():
    """Select a course, input marks for students in this course."""
    if not courses:
        print("\nNo courses available. Please add courses first.")
        return
    if not students:
        print("\nNo students available. Please add students first.")
        return

    list_courses()
    course_id = input("\nEnter Course ID to input marks: ").strip()

    # Verify course exists
    valid_courses = [c["id"] for c in courses]
    if course_id not in valid_courses:
        print(f"Error: Course ID '{course_id}' not found.")
        return

    if course_id not in marks:
        marks[course_id] = {}

    print(f"\n--- Entering marks for course: {course_id} ---")
    for student in students:
        while True:
            try:
                score = float(input(f"Enter mark for {student['name']} (ID: {student['id']}): "))
                if 0 <= score <= 20:  # standard USTH/French grading scale (0 to 20)
                    marks[course_id][student["id"]] = score
                    break
                print("Mark must be between 0 and 20.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")


# ------------------ Listing Functions ------------------

def list_courses():
    """List all courses."""
    if not courses:
        print("\nNo courses to display.")
        return
    print("\n========== Courses List ==========")
    for c in courses:
        print(f"ID: {c['id']:<10} | Name: {c['name']}")
    print("==================================")


def list_students():
    """List all students."""
    if not students:
        print("\nNo students to display.")
        return
    print("\n======================= Students List =======================")
    for s in students:
        print(f"ID: {s['id']:<10} | Name: {s['name']:<20} | DoB: {s['dob']}")
    print("=============================================================")


def show_student_marks():
    """Show student marks for a given course."""
    if not courses:
        print("\nNo courses available.")
        return

    list_courses()
    course_id = input("\nEnter Course ID to view marks: ").strip()

    if course_id not in [c["id"] for c in courses]:
        print(f"Error: Course ID '{course_id}' not found.")
        return

    if course_id not in marks or not marks[course_id]:
        print(f"No marks recorded for Course ID '{course_id}'.")
        return

    print(f"\n========== Marks for Course: {course_id} ==========")
    for student in students:
        s_id = student["id"]
        score = marks[course_id].get(s_id, "N/A")
        print(f"ID: {s_id:<10} | Name: {student['name']:<20} | Mark: {score}")
    print("=================================================")


# ------------------ Main Menu ------------------

def main():
    while True:
        print("\n" + "=" * 40)
        print("  STUDENT MARK MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks for a course")
        print("0. Exit")
        choice = input("Enter your choice (0-6): ").strip()

        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_marks_for_course()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_student_marks()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please choose between 0 and 6.")


if __name__ == "__main__":
    main()
