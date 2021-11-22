"""
This module contains classes of custom  Exception for Homeworks in class Student
"""


class HomeworkException(Exception):
    """
    Exception for check Homework contains in Homework collections of Students
    """
    pass


class HomeworkStatusException(Exception):
    """
       Exception for check Homework status contains in Homework collections of Students ( bool - Homework Done - True,
       Homework Empty - False)
       """
    pass
