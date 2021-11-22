"""
This module contains Teacher class definition

class Teacher inherited from Person

"""

from person import Person


class Teacher(Person):
    def __init__(self, name, age):
        """
        Describe of Teacher

        @param name: name of Teacher
        @param age: age of Teacher
        @param score: score of Teacher
        @param courses: list -  courses in which the Teacher teaches
        """
        super().__init__(name, age)
        self.score = 0
        self.courses = []

    def __str__(self):
        return super().__str__() + f"{self.age} | {self.score} | {self.courses}"

    def add_courses(self, course):
        """
        Add courses in which the Teacher teaches
        @param course: course object from courses collection
        """
        self.courses = course
