"""
This module contains Employee class definition

class Employee inherited from Person

"""

from person import Person


class Employee(Person):
    __slots__ = "_room"

    def __init__(self, name, age):
        """
        Describe of Employee
        @param name: name of Employee
        @param age: age of Employee
        """
        super().__init__(name, age)
        self._room = 0

    def __str__(self):
        return super().__str__() + f"{self._age} | {self._room} "

    def __repr__(self):
        return super().__str__() + f"{self._age} | {self._room} "

    def __eq__(self, other):
        return isinstance(other, Employee) and self._name == other._name \
               and self._age == other._age