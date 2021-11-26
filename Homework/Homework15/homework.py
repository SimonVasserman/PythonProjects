"""
This module contains Homework class definition


"""


class Homework:
    __slots__ = "name", "description", "complexity", "status"

    def __init__(self, name, description, complexity, status):
        """
         Describe of Homework
        @param name: name of Homework
        @param description: short information about this Homework
        @param complexity: level of homework complexity
        @param status: status of Homework ( True - Done, False - Empty)
        """
        self.name = name
        self.description = description
        self.complexity = complexity
        self.status = status

    def __repr__(self):
        return f"{self.name} | {self.status} "

    def __str__(self):
        return f"{self.name} | {self.status} "

    def __eq__(self, other):
        return isinstance(other, Homework) and self._name == other._name