# DZ7.1
def calculate(a, b):
    return a + b, a - b


print(calculate(50, 20))


##########################################
# DZ7.2

def sum(my_list):
    sum = 0
    for item in my_list:
        sum += item
    return sum


l1 = [57, 79, 44, 16, 43, 96, 32, 44, 66, 9]
print(sum(l1))


############################################
# DZ7.3

def func(*args):
    for item in range(len(args)):
        print(args[item], item)


func(34, 2544, 443, 655, 765)


############################################
#  DZ7.4


def showEmployee(name, salary=9000):
    print(name, salary)


showEmployee("Anton", )
showEmployee("Mark", 26000)
showEmployee("Amelie", 14000)
