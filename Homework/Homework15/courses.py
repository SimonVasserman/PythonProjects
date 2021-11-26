"""
This module contains Course class definition

"""


class Course:
    __slots__ = "__name", "__description", "__start_date", "__end_date", "__quantity_lesson"

    def __init__(self, name, description, star_date, end_date, quantity_lesson):
        """
        Describe of Course
        @param name: name of Course
        @param description: short information  about this Course
        @param star_date: date of start lessons of this Course
        @param end_date: date of finish lessons of this Course
        @param quantity_lesson: quantity of lessons that contains this Course
        """
        self.__name = name
        self.__description = description
        self.__start_date = star_date
        self.__end_date = end_date
        self.__quantity_lesson = quantity_lesson

    def __repr__(self):
        return f"{self.__name} | {self.__description} | {self.__start_date}-{self.__end_date} |" \
               f" lessons:{self.__quantity_lesson} "

    def __str__(self):
        return f"{self.__name} | {self.__description} | {self.__start_date}-{self.__end_date} |" \
               f" lessons:{self.__quantity_lesson} "

    def __eq__(self, other):
        return isinstance(other, Course) and self.__name == other._name
