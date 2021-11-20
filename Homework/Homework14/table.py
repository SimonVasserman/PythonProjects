from prettytable import PrettyTable

resultTable = PrettyTable()


class Table:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def __str__(self):
        return self.name

    def add_student(self, student_obj):
        self.students.append(student_obj)

    def add_teacher(self, teacher_obj):
        self.students.append(teacher_obj)

    def get_summary(self):
        summary = []
        for student in self.students:
            summary.append(
                [
                    student.name,
                    student.age,
                    student.grade,
                    student.subscribed_courses,
                    student.homeworks,])

        for teacher in self.teachers:
            summary.append(
                    [
                        teacher.name,
                        teacher.age,
                        teacher.score,
                        teacher.courses,
                    ]
                )
        return summary

    def get_summary_table(self):
        resultTable.field_names = [
            "Name",
            "Age",
            "Grade",
            "Subscribed courses",
            "Homeworks",
        ]
        for student in self.students:
            resultTable.add_row(
                [
                    student.name,
                    student.age,
                    student.grade,
                    student.subscribed_courses,
                    student.homeworks,
                ]
            )
            for teacher in self.teachers:
                resultTable.add_row(
                    [
                        teacher.name,
                        teacher.age,
                        teacher.score,
                        teacher.subscribed_courses,
                        student.homeworks,
                    ]
                )
        return resultTable
