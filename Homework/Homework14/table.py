"""
class Table contains functions to create a table
with information about students (their names, ages, their courses, homework, their grades),
teachers (their names, ages, courses, and their scores)
and also about employees (their names, ages, rooms)

This class uses the module prettyTable import PrettyTable for creating a table for information


"""

from prettytable import PrettyTable

resultTable = PrettyTable()
resultTable_t = PrettyTable()
resultTable_e = PrettyTable()


class Table:
    def __init__(self, name):
        """

        @param name: Name of Students, Teachers and Employees
        """
        self.name = name
        self.students = []
        self.teachers = []
        self.employees = []

    def __str__(self):
        """

        @return: name of Students, Teachers and Employees
        """
        return self.name

    def add_student(self, student_obj):
        """
        This function adds students to the table
        @param student_obj: student object from school(list)  in file -> main.py
        """
        self.students.append(student_obj)

    def add_teacher(self, teacher_obj):
        """
        This function adds teachers to the table
        @param teacher_obj: teacher  object from teachers(list)  in file -> main.py
        """
        self.teachers.append(teacher_obj)

    def add_employee(self, employee_obj):
        """
        This function adds teachers to the table
        @param employee_obj: teacher  object from teachers(list)  in file -> main.py
        """
        self.employees.append(employee_obj)

    def get_summary(self):
        """
        This function creates append  of all parameters for each student in empty list of summary
        @return: complete summary  list
        """
        summary = []
        for student in self.students:
            summary.append(
                [
                    student.name,
                    student.age,
                    student.grade,
                    student.subscribed_courses,
                    student.homeworks,
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
        for student in self.students:
            resultTable.add_row(
                [
                    student.name,
                    student.age,
                    student.grade,
                    student.subscribed_courses,
                    student.homeworks
                ]
            )
        return resultTable

    def get_teacher_summary(self):
        """
        This function creates append  of all parameters for each teachers in empty list of teacher_summary
        @return: complete teacher_summary  list
        """
        teacher_summary = []
        for teacher in self.teachers:
            teacher_summary.append(
                [
                    teacher.name,
                    teacher.age,
                    teacher.score,
                    teacher.courses,
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
        for teacher in self.teachers:
            resultTable_t.add_row(
                [
                    teacher.name,
                    teacher.age,
                    teacher.score,
                    teacher.courses,
                ]
            )
        return resultTable_t

    def get_employee_summary(self):
        """
        This function creates append  of all parameters for each teachers in empty list of teacher_summary
        @return: complete employee_summary  list
        """
        employee_summary = []
        for employee in self.employees:
            employee_summary.append(
                [
                    employee.name,
                    employee.age,
                    employee.room,
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
        for employee in self.employees:
            resultTable_e.add_row(
                [
                    employee.name,
                    employee.age,
                    employee.room,
                ]
            )
        return resultTable_e
