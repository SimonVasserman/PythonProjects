"""
This module contains Homework class definition


"""


class Homework:
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
        return f"{self.name} | {self.status}"
