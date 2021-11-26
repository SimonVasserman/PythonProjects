"""
This module contains Person class definition

class Person base class for Student, Teacher, Employee

"""


class Person:
    def __init__(self, name, age):
        """
        Describe of Person
        @param name: name of Person
        @param age: age of Person
        """
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}\nage: {self.age}"
