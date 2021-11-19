import unit_test_framework as utf
from employee import Employee
from teacher import Teacher
from homework import Homework
from student import Student


school = [Student("Ivan", 25, 0),
          Student("Ivan 2", 25, 0),
          Student("Ivan 3", 25, 0)]

h = Homework("OOP intorduction",
             "Extend logic for Student program",
             2,
             False)

print("Student ->", school[0])
t = Teacher("Fedor", 31)
print("Teacher ->",t)
e = Employee("Sidor", 45)
print("Employee ->", e)

exit(0)

for student in school:
    student.add_homework(h)

print(school[0].is_homework_done())


