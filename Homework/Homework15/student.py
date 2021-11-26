"""
This module contains Student class definition

class Student inherited from Person
exception:
    HomeworkException
    HomeworkStatusException

"""
from person import Person
from school_exceptions import HomeworkException, HomeworkStatusException


class Student(Person):
    __slots__ = "_grade", "_subscribed_courses", "_homeworks"

    def __init__(self, name, age, grade):
        """
        Describe of Student

        @param  name: name of  Student
        @param age: age of Student
        @param grade: grade of Student
        """
        super().__init__(name, age)
        self._grade = grade
        self._subscribed_courses = []
        self._homeworks = {}

    def __repr__(self):
        return f"{self._name} | {self._age} | {self._homeworks} | {self._subscribed_courses}"

    def add_homework(self, hw_number, homework):
        """
        Add new homework object to the self.homeworks collection
        @raise HomeworkStatusException
        @param hw_number: number of homework in self.homeworks collection
        @param homework: homework object in self.homeworks collection
        """
        self._homeworks[hw_number] = homework

    def is_homework_done(self, hw_number):
        """
        @raise HomeworkException
        @param hw_number: number of homework in self.homeworks collection
        @return:
        """
        if len(self._homeworks) == 0:
            raise HomeworkException("Homeworks is empty")
        current_hw = self._homeworks.get(hw_number)
        if current_hw:
            return current_hw.status
        return HomeworkStatusException("No such homework")

    def change_homework_status(self, hw_number, status=True):
        """
        Change homework status, then Student did homework or not did

        @param hw_number: number of homework in self.homeworks collection
        @param status: status of homework True - Done, False - Empty
        @return: status
        @raise HomeworkStatusException

        """
        current_hw = self._homeworks.get(hw_number)
        if current_hw:
            current_hw.status = status
            return current_hw
        return HomeworkStatusException("No such homework")

    def add_sub_courses(self, course):
        """
        Add courses to which the Student is subscribed
        @param course: course object from courses collection
        """
        self._subscribed_courses = course



