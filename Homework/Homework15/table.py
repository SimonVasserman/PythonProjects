"""
class Table contains functions to create a table
with information about students (their names, ages, their courses, homework, their grades),
teachers (their names, ages, courses, and their scores)
and also about employees (their names, ages, rooms)

This module  uses  prettytable for creating a Table in Python Console

"""
from prettytable import prettytable

resultTable = prettytable.PrettyTable()
resultTable_t = prettytable.PrettyTable()
resultTable_e = prettytable.PrettyTable()


class Table:
    __slots__ = "_name", "_students", "_teachers", "_employees"

    def __init__(self, name):
        """
        Describe of Table
        @param name: Name of Students, Teachers and Employees
        """
        self._name = name
        self._students = []
        self._teachers = []
        self._employees = []

    def __str__(self):
        """
        Describe of Table
        @return: name of Students, Teachers and Employees
        """
        return self._name

    def __repr__(self):
        """
        Describe of Table
        @return: name of Students, Teachers and Employees
        """
        return self._name

    def __eq__(self, other):
        return isinstance(other, Table) and self._name == other._name

    def add_student(self, student_obj):
        """
        This function adds students to the table
        @param student_obj: student object from school(list)  in file -> main.py
        """
        self._students.append(student_obj)

    def add_teacher(self, teacher_obj):
        """
        This function adds teachers to the table
        @param teacher_obj: teacher  object from teachers(list)  in file -> main.py
        """
        self._teachers.append(teacher_obj)

    def add_employee(self, employee_obj):
        """
        This function adds teachers to the table
        @param employee_obj: teacher  object from teachers(list)  in file -> main.py
        """
        self._employees.append(employee_obj)

    def get_summary(self):
        """
        This function creates append  of all parameters for each student in empty list of summary
        @return: complete summary  list
        """
        summary = []
        for student in self._students:
            summary.append(
                [
                    student._name,
                    student._age,
                    student._grade,
                    student._subscribed_courses,
                    student._homeworks,
                ]
            )
        return summary

    def get_summary_table(self):
        """
        This function creates a table row with field_names ("Name","Age","Grade","Subscribed courses",
            "Homeworks"), and also creates rows with students information
         @return: table contains students information
        """
        resultTable.field_names = [
            "Name",
            "Age",
            "Grade",
            "Subscribed courses",
            "Homeworks"
        ]
        for student in self._students:
            resultTable.add_row(
                [
                    student._name,
                    student._age,
                    student._grade,
                    student._subscribed_courses,
                    student._homeworks
                ]
            )
        return resultTable

    def get_teacher_summary(self):
        """
        This function creates append  of all parameters for each teachers in empty list of teacher_summary
        @return: complete teacher_summary  list
        """
        teacher_summary = []
        for teacher in self._teachers:
            teacher_summary.append(
                [
                    teacher._name,
                    teacher._age,
                    teacher._score,
                    teacher._courses,
                ]
            )
        return teacher_summary

    def get_summary_teacher_table(self):
        """
        This function creates a table row with field_names ("Name","Age","Score","Courses",),
         and also creates rows with teachers information
        @return: table contains teachers information
        """
        resultTable_t.field_names = [
            "Name",
            "Age",
            "Score",
            "Courses",
        ]
        for teacher in self._teachers:
            resultTable_t.add_row(
                [
                    teacher._name,
                    teacher._age,
                    teacher._score,
                    teacher._courses,
                ]
            )
        return resultTable_t

    def get_employee_summary(self):
        """
        This function creates append  of all parameters for each teachers in empty list of teacher_summary
        @return: complete employee_summary  list
        """
        employee_summary = []
        for employee in self._employees:
            employee_summary.append(
                [
                    employee._name,
                    employee._age,
                    employee._room,
                ]
            )
        return employee_summary

    def get_summary_employee_table(self):
        """
        This function creates a table row with field_names ("Name","Age","Room"),
         and also creates rows with employees information
        @return: table contains employees information
        """
        resultTable_e.field_names = [
            "Name",
            "Age",
            "Room",
        ]
        for employee in self._employees:
            resultTable_e.add_row(
                [
                    employee._name,
                    employee._age,
                    employee._room,
                ]
            )
        return resultTable_e
