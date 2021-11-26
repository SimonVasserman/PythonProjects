"""
This module contains Employee class definition

class Employee inherited from Person

"""

from person import Person


class Employee(Person):
    def __init__(self, name, age):
        """
        Describe of Employee
        @param name: name of Employee
        @param age: age of Employee
        """
        super().__init__(name, age,)
        self.room = 0

    def __str__(self):
        return super().__str__() + f"{self.age} | {self.room} "
