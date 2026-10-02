from .person import Person


class Student(Person):
    """Student class representing an enrolled student."""

    def __init__(self, student_id: str = "", name: str = "", dob: str = ""):
        super().__init__(student_id, name, dob)

    def __str__(self) -> str:
        return f"Student[ID={self.get_id()}, Name={self.get_name()}, DoB={self.get_dob()}]"
