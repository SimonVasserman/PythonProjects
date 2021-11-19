import unit_test_framework as utf
from employee import Employee
from teacher import Teacher
from homework import Homework
from student import Student
from table import Table

school = [Student("Ivan", 25, 0), Student("Peter", 28, 0), Student("Marina", 17, 0), Student("Bogdan", 20, 0)]

hw = Homework("OOP intorduction", "Extend logic for Student program", 2, False)
hw2 = Homework("Python web", "Extend logic for Student program", 2, False)
hw3 = Homework("OOP Part 3", "Create function to output information about students,status of homeworks", 3, False)
table = Table(name="Intro Python")
table_b = Table(name="Python web")

for student in school:
    student.add_homework(1, hw)
    student.add_homework(2, hw2)
    student.add_homework(3, hw3)
    table.add_student(student)

summary = table.get_summary()
for item in summary:
    print(item)

print(table.get_summary_table())
print("Student ->", school[0])
t = Teacher("Fedor", 31)
print("Teacher ->", t)
e = Employee("Sidor", 45)
print("Employee ->", e)

exit(0)

print(school[0].is_homework_done())

