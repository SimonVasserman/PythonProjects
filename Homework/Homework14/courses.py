"""
This module contains Course class definition

"""


class Course:
    def __init__(self, name, description, star_date, end_date, quantity_lesson):
        """
        Describe of Course
        @param name: name of Course
        @param description: short information  about this Course
        @param star_date: date of start lessons of this Course
        @param end_date: date of finish lessons of this Course
        @param quantity_lesson: quantity of lessons that contains this Course
        """
        self.name = name
        self.description = description
        self.start_date = star_date
        self.end_date = end_date
        self.quantity_lesson = quantity_lesson

    def __repr__(self):
        return f"{self.name} | {self.description} | {self.start_date}-{self.end_date} | lessons:{self.quantity_lesson}"
