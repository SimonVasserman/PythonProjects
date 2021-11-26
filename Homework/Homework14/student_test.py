"""
This module contains class StudentTest,
which contains testing functions for testing class Student

This module importing unit_test_framework as utf

"""
import unit_test_framework.expectations as utf
from homework import Homework
from student import Student
from school_exceptions import HomeworkStatusException


class StudentTest:

    def __init__(self):
        """
        Describe a test Student
        @param test_name: name of testing Student
        @param test_age: age of  testing Student
        @param test_grade: grade of testing  Student
        @param test_student: Student object
        """
        self.test_name = "test_name"
        self.test_age = "99"
        self.test_grade = 650
        self.test_student = Student("", 0, 0)

    def StudentTestSetUp(self):
        """
        Set up of testing Student
        """
        self.test_student = Student(self.test_name, self.test_age, self.test_grade)

    def Student_Name_Test_1(self):
        """
        Check of Student name actual = expected
        """
        self.StudentTestSetUp()
        actual = self.test_student.name
        expected = self.test_name
        utf.ExpectEqual(actual, expected)

    def Student_Age_Test_1(self):
        """
        Check of Student age actual = expected
        """
        self.StudentTestSetUp()
        actual = self.test_student.age
        expected = self.test_age
        utf.ExpectEqual(actual, expected)

    def Student_Grade_Test_1(self):
        """
        Check of Student grade actual = expected
        """
        self.StudentTestSetUp()
        actual = self.test_student.grade
        expected = self.test_grade
        utf.ExpectEqual(actual, expected)

    def Student_AddHomework_Test_1(self):
        """
        Check of adding a Homework to  Student
        """
        self.StudentTestSetUp()
        self.test_student.add_homework(Homework("", "", 0, 0))
        actual = len(self.test_student.homeworks)
        expected = 1
        utf.ExpectEqual(actual, expected)

    def Student_AddHomework_Test_2(self):
        """
        Check of adding of three of Homework to Student
        """
        self.StudentTestSetUp()
        self.test_student.add_homework(Homework("", "", 0, 0))
        self.test_student.add_homework(Homework("", "", 0, 0))
        self.test_student.add_homework(Homework("", "", 0, 0))
        actual = len(self.test_student.homeworks)
        expected = 3
        utf.ExpectEqual(actual, expected)

    def Student_AddHomework_Test_3(self):
        """
        Check of empty Homework at Student
        """
        self.StudentTestSetUp()
        actual = len(self.test_student.homeworks)
        expected = 0
        utf.ExpectEqual(actual, expected)

    def Student_AddHomework_Exception_Test_1(self):
        """
        Check that when adding Homework that the Student does not already have this Homework
        """
        self.StudentTestSetUp()

        def block():
            """
            If it happened to block and generate an error
            """
        self.test_student.add_homework(Homework("", "", 0, True))

        utf.ExpectThrown(block, HomeworkStatusException())


student_test = StudentTest()

student_test.Student_AddHomework_Test_1()
student_test.Student_AddHomework_Test_2()
student_test.Student_AddHomework_Test_3()
student_test.Student_Name_Test_1()
student_test.Student_Age_Test_1()
student_test.Student_Grade_Test_1()
student_test.Student_AddHomework_Exception_Test_1()


