"""
Domain entity: Course
"""

class Course:
    """Represents an academic course with credits."""

    def __init__(self, course_id: str = "", name: str = "", credits: int = 1):
        self.__id = course_id
        self.__name = name
        self.__credits = credits

    # Getters and Setters
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

    def __str__(self) -> str:
        return f"Course[ID={self.__id}, Name={self.__name}, Credits={self.__credits}]"
