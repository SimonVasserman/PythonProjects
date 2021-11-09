# DZ10.1

import random

# numbers = open("numbers.txt", "wt")
#
# for i in range(1, 901):
#     numbers.write(str(random.randint(1, 100)) + " ")
#     if i % 9 == 0:
#         numbers.write(str(random.randint(1, 100)) + "\n")
# numbers.close()

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
            result = [int(value)**2 for value in line.split()]
            file.write(" ".join(map(str, result)) + '\n')


read_and_add("numbers")

#tests



