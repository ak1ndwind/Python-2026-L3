
# INPUT FUNCTIONS

def input_number_of_students():
    """Input and validate the number of students in a class."""
    while True:
        try:
            num = int(input("Enter number of students in class: "))
            if num <= 0:
                print("Please enter a positive integer greater than 0.")
                continue
            return num
        except ValueError:
            print("Invalid input! Please enter an integer.")


def input_student_info():
    """
    Input information for a single student.
    Returns student data as a dictionary.
    """
    student_id = input("  Enter Student ID: ").strip()
    name = input("  Enter Student Name: ").strip()
    dob = input("  Enter Date of Birth (DD/MM/YYYY): ").strip()
    
    # Store student attributes in a dictionary
    return {
        "id": student_id,
        "name": name,
        "dob": dob
    }


def input_all_students():
    """Input a batch of students based on the total student count."""
    students = []
    count = input_number_of_students()
    for i in range(count):
        print(f"\n--- Student {i + 1}/{count} ---")
        student = input_student_info()
        students.append(student)
    print(f"\nSuccessfully added {len(students)} student(s).")
    return students


def input_number_of_courses():
    """Input and validate the number of courses."""
    while True:
        try:
            num = int(input("Enter number of courses: "))
            if num <= 0:
                print("Please enter a positive integer greater than 0.")
                continue
            return num
        except ValueError:
            print("Invalid input! Please enter an integer.")


def input_course_info():
    """
    Input information for a single course.
    Returns course data as a dictionary.
    """
    course_id = input("  Enter Course ID: ").strip()
    course_name = input("  Enter Course Name: ").strip()
    
    return {
        "id": course_id,
        "name": course_name
    }


def input_all_courses():
    """Input a batch of courses based on total course count."""
    courses = []
    count = input_number_of_courses()
    for i in range(count):
        print(f"\n--- Course {i + 1}/{count} ---")
        course = input_course_info()
        courses.append(course)
    print(f"\nSuccessfully added {len(courses)} course(s).")
    return courses


def input_marks_for_course(courses, students, marks):
    """
    Select a course, then input marks for all students in that course.
    Marks are stored in a dictionary keyed by (course_id, student_id) tuple
    or marks[course_id][student_id].
    """
    if not courses:
        print("\n[!] No courses available. Please add courses first.")
        return

    if not students:
        print("\n[!] No students available. Please add students first.")
        return

    print("\n--- Available Courses ---")
    list_courses(courses)
    
    course_id = input("\nEnter Course ID to input marks for: ").strip()
    
    # Validate course existence
    selected_course = None
    for c in courses:
        if c["id"] == course_id:
            selected_course = c
            break

    if selected_course is None:
        print(f"[!] Course with ID '{course_id}' not found.")
        return

    # Ensure course exists in marks dict
    if course_id not in marks:
        marks[course_id] = {}

    print(f"\nEntering marks for course: {selected_course['name']} ({course_id})")
    for student in students:
        s_id = student["id"]
        s_name = student["name"]
        
        while True:
            try:
                score = float(input(f"  Enter mark for {s_name} (ID: {s_id}) [0-20]: "))
                if 0.0 <= score <= 20.0:
                    marks[course_id][s_id] = score
                    break
                else:
                    print("  [!] Mark must be between 0 and 20.")
            except ValueError:
                print("  [!] Please enter a valid numerical value.")

    print(f"\nMarks updated successfully for course: {selected_course['name']}.")


# LISTING FUNCTIONS

def list_courses(courses):
    """List all available courses."""
    if not courses:
        print("\n[!] No courses to display.")
        return

    print("\n" + "=" * 45)
    print(f"{'No.':<5} {'Course ID':<15} {'Course Name':<25}")
    print("-" * 45)
    for idx, course in enumerate(courses, start=1):
        # Pack info into a tuple for clean formatting
        info_tuple = (idx, course["id"], course["name"])
        print(f"{info_tuple[0]:<5} {info_tuple[1]:<15} {info_tuple[2]:<25}")
    print("=" * 45)


def list_students(students):
    """List all registered students."""
    if not students:
        print("\n[!] No students to display.")
        return

    print("\n" + "=" * 55)
    print(f"{'No.':<5} {'Student ID':<15} {'Student Name':<20} {'DoB':<15}")
    print("-" * 55)
    for idx, student in enumerate(students, start=1):
        # Using a tuple representation for each record
        record = (idx, student["id"], student["name"], student["dob"])
        print(f"{record[0]:<5} {record[1]:<15} {record[2]:<20} {record[3]:<15}")
    print("=" * 55)


def show_student_marks(courses, students, marks):
    """Show marks of all students for a selected course."""
    if not courses:
        print("\n[!] No courses available.")
        return

    if not students:
        print("\n[!] No students available.")
        return

    print("\n--- Available Courses ---")
    list_courses(courses)
    
    course_id = input("\nEnter Course ID to view marks: ").strip()
    
    selected_course = None
    for c in courses:
        if c["id"] == course_id:
            selected_course = c
            break

    if selected_course is None:
        print(f"[!] Course with ID '{course_id}' not found.")
        return

    if course_id not in marks or not marks[course_id]:
        print(f"[!] No marks have been recorded yet for course '{selected_course['name']}'.")
        return

    print("\n" + "=" * 55)
    print(f"Marks for Course: {selected_course['name']} ({course_id})")
    print("-" * 55)
    print(f"{'Student ID':<15} {'Student Name':<25} {'Mark':<10}")
    print("-" * 55)
    
    course_marks = marks[course_id]
    for student in students:
        s_id = student["id"]
        s_name = student["name"]
        score = course_marks.get(s_id, "N/A")
        
        # Display as a tuple of (ID, Name, Mark)
        item = (s_id, s_name, f"{score:.2f}" if isinstance(score, float) else score)
        print(f"{item[0]:<15} {item[1]:<25} {item[2]:<10}")
        
    print("=" * 55)

# MAIN APPLICATION LOOP

def main():
    """Main interactive menu driver."""
    # Data storage using lists and dicts (no classes)
    students = []
    courses = []
    marks = {}  # {course_id: {student_id: mark}}

    while True:
        print("\n" + "=" * 45)
        print("  STUDENT MARK MANAGEMENT SYSTEM")
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
            students.extend(input_all_students())
        elif choice == "2":
            courses.extend(input_all_courses())
        elif choice == "3":
            input_marks_for_course(courses, students, marks)
        elif choice == "4":
            list_students(students)
        elif choice == "5":
            list_courses(courses)
        elif choice == "6":
            show_student_marks(courses, students, marks)
        elif choice == "0":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\n[!] Invalid choice! Please enter a number between 0 and 6.")


if __name__ == "__main__":
    main()