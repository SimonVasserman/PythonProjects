"""
This module contains of helping functions for sorting Students

"""


def sort_students_by_age(student):
    """
    This functions sort Students by age argument
    @param student: students object in school list collection
    @return: sorted  school list by age of Students
    """
    sorted(school, key=lambda student: student.age)
    return student.age


def sort_students_by_grade(student):
    """
    This functions sort Students by grade argument
    @param student: students object in school list collection
    @return: sorted  school list by grade of Students
    """
    sorted(school, key=lambda student: student.grade)
    return student.grade
