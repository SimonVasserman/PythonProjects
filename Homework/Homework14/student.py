from person import Person
from school_exceptions import HomeworkException, HomeworkStatusException


class Student(Person):
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.subscribed_courses = []
        self.homeworks = {}

    def __repr__(self):
        return f"{self.name} | {self.age} | {self.homeworks}"

    def add_homework(self, hw_number, homework):
        self.homeworks[hw_number] = homework

    def is_homework_done(self, hw_number):
        if len(self.homeworks) == 0:
            raise Exception("Homeworks is empty")
        current_hw = self.homeworks.get(hw_number)
        if current_hw:
            return current_hw.status
        return Exception("No such homework")

    def change_homework_status(self, hw_number, status=True):
        current_hw = self.homeworks.get(hw_number)
        if current_hw:
            current_hw.status = status
            return current_hw
        return Exception("No such homework")


