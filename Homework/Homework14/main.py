import unit_test_framework as utf
from employee import Employee
from teacher import Teacher
from homework import Homework
from student import Student
from table import Table
from courses import Course

school = [Student("Ivan", 25, 0), Student("Peter", 28, 0), Student("Marina", 17, 0), Student("Bogdan", 20, 0),
          Student("Artem", 23, 0), Student("Maria", 21, 0), Student("Mike", 27, 0), Student("Nikita", 24, 0),
          Student("Artur", 21, 0), Student("Julia", 26, 0), Student("Anton", 29, 0), Student("Ludmila", 30, 0),
          Student("Maxim", 32, 0), Student("Andrey", 19, 0)]

teachers = [Teacher("Fedor", 35), Teacher("Vladimir", 40)]
employees = [Employee("Viktor", 32,)]

hw = Homework("OOP Introduction", "Extend logic for Student program", 2, False)
hw2 = Homework("Python web", "Extend logic for Student program", 2, False)
hw3 = Homework("OOP Part 3", "Create function to output information about students,status of homeworks", 3, False)
table = Table(name="Intro Python")
table_b = Table(name="Python web")

courses = [Course("Introduction Python", "Basic Python", 29.09, 16.11, 16),
           Course("Advanced Python", "Python", 02.01, 16.05, 32),
           Course("Machine Learning", "Python", 10.01, 10.05, 20)]

for student in school:
    student.add_homework(1, hw)
    student.add_homework(2, hw2)
    student.add_homework(3, hw3)
    student.change_homework_status(1, True)
    student.add_sub_courses(courses[0])
    table.add_student(student)

for teacher in teachers:
    teacher.add_courses(courses[0:2])
    teachers[1].add_courses(courses)
    table.add_teacher(teacher)

for employee in employees:
    table.add_employee(employee)

summary = table.get_summary()
teacher_summary = table.get_teacher_summary()
employee_summary = table.get_employee_summary()

for item in summary:
    print(item)

for item in teacher_summary:
    print(item)

for item in employee_summary:
    print(item)

print(table.get_summary_teacher_table())
print(table.get_summary_table())
print(table.get_summary_employee_table())

print(courses[0].__str__())
print(courses[1].__str__())
print(courses[2].__str__())

# print("Student ->", school[0])
# t = Teacher("Fedor", 31)
# print("Teacher ->", t)
# e = Employee("Viktor", 45)
# print("Employee ->", e)
#
# exit(0)
#
# print(school[0].is_homework_done())
