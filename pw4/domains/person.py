class Person:
    """Base class for any person in the system."""

    def __init__(self, person_id: str = "", name: str = "", dob: str = ""):
        self.__id = person_id
        self.__name = name
        self.__dob = dob

    # Getters and Setters
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

    def __str__(self) -> str:
        return f"Person[ID={self.__id}, Name={self.__name}, DoB={self.__dob}]"
