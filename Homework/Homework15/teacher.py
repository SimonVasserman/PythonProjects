"""
This module contains Teacher class definition

class Teacher inherited from Person

"""

from person import Person


class Teacher(Person):
    __slots__ = "_score", "_courses"

    def __init__(self, name, age):
        """
        Describe of Teacher

        @param name: name of Teacher
        @param age: age of Teacher
        @param score: score of Teacher
        @param courses: list -  courses in which the Teacher teaches
        """
        super().__init__(name, age)
        self._score = 0
        self._courses = []

    def __str__(self):
        return super().__str__() + f"{self._age} | {self._score} | {self._courses}"

    def add_courses(self, course):
        """
        Add courses in which the Teacher teaches
        @param course: course object from courses collection
        """
        self._courses = course
