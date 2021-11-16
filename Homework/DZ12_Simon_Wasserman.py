class Homework:
    def __init__(self, name, description, complexity, status):
        self.name = name
        self.description = description
        self.complexity = complexity
        self.status = status


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.subscribed_courses = []
        self.homeworks = []

    def add_homework(self, homework):
        # if homework.status == 1:
        #     raise Exception
        self.homeworks.append(homework)

    def is_homework_done(self):
        if len(self.homeworks) == 0:
            raise Exception("Homeworks is empty")
        return self.homeworks[0].status

    def change_status_homework(self, homework):
        pass


def sort_students_by_age(students):
    sorted(school, key=lambda student: student.age)
    return student.age


def sort_students_by_grade(students):
    sorted(school, key=lambda student: student.grade)
    return student.grade



class Table(Student)
    def __init__(self):
        print("")


school = [Student("Ivan", 25, 0),
          Student("Ivan 2", 25, 0),
          Student("Ivan 3", 25, 0)]

h = Homework("OOP introduction",
             "Extend logic for Student program",
             2, False)
h1 = Homework("OOP Part 2",
              "Create class Table for all students",
              4, False)
h2 = Homework("OOP Part 3",
              "Create function to output information about students,status of homeworks",
              3, False)

for student in school:
    student.add_homework(h)
    student.add_homework(h1)
    student.add_homework(h2)

print(school[0].is_homework_done())


