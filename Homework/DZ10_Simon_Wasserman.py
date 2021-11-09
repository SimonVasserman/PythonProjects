# DZ10.1
import random


def create_and_write(filename):
    with open(f"{filename}.txt", "w") as file:
        strings = []
        for _ in range(100):
            random_list = random.sample(range(100), 10)
            random_string = " ".join(map(str, random_list)) + '\n'
            strings.append(random_string)
        file.writelines(strings)


create_and_write('numbers')


# DZ10.2

def read_and_add(filename):
    with open(f"{filename}.txt", "r+") as file:
        my_list = file.readlines()
        for line in my_list:
            result = [int(value) ** 2 for value in line.split()]
            file.write(" ".join(map(str, result)) + '\n')


read_and_add("numbers")

# tests

create_and_write('test1')
read_and_add('test1')

create_and_write('test2')
read_and_add('test2')

create_and_write('test3')
read_and_add('test3')

create_and_write('test4')
read_and_add('test4')

create_and_write('test5')
read_and_add('test5')
