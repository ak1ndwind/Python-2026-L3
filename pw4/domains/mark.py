class StudentMark:
    """Associates a student and a course with a grade."""

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
