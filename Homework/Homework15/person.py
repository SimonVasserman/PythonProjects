"""
This module contains Person class definition

class Person base class for Student, Teacher, Employee

"""


class Person:
    __slots__ = "_name", "_age"

    def __init__(self, name, age):
        """
        Describe of Person
        @param name: name of Person
        @param age: age of Person
        """
        self._name = name
        self._age = age

    def __str__(self):
        return f"Name: {self._name}\nage: {self._age}"

    @property
    def name(self):
        return self._name
