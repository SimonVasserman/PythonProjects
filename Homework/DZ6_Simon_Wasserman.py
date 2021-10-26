print("DZ6.1")
import random
my_list1 = tuple((random.randint(0, 100)) for i in range(10))
print("result")
print(my_list1)
#########################################################
print("DZ6.2")
import random
my_list2 = [(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)) for i in range(3)]
print(my_list2)
my_list2 = ([t[:-1] + (100,) for t in my_list2])
print("result")
print(my_list2)
########################################################
print("DZ6.3V1")
l3_1 = [(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)) for i in range(4)]
print(l3_1)
res = [0, 0, 0, 0]
for i in range(len(l3_1)):
    for n in range(len(l3_1[i])):
        res[n] += l3_1[i][n]
res = tuple(res)
print("result")
print(res)
########################################################
print("DZ6.3V2")
import random
l1_2 = tuple((random.randint(1,5)) for i in range(4))
l2_2 = tuple((random.randint(1,5)) for i in range(4))
l3_2 = tuple((random.randint(1,5)) for i in range(4))
print(l1_2, l2_2, l3_2)
res = [a+b+c for a, b, c in zip(l1_2, l2_2, l3_2)]
res = tuple(res)
print("result")
print(res)
########################################################
print("DZ6.4")
a = int(input(" Введите число :"))
import random
s = set()
for i in range(10):
  s.add(random.randint(0, 10))
print(s)
print("result")
if a in s:
    print("True")
else:
    print("False")
########################################################
print("DZ6.5")
import random
s1 = set()
for i in range(10):
  s1.add(random.randint(0, 10))
s2 = set()
for i in range(10):
  s2.add(random.randint(0, 10))
print(s1, s2)
result = s1 & s2
print("result")
print(result)
########################################################
print("DZ6.6")
import random
s3 = set()
for i in range(10):
  s3.add(random.randint(0, 10))
s4 = set()
for i in range(10):
  s4.add(random.randint(0, 10))
print(s3, s4)
result1 = s3.difference(s4)
print("result")
print(result1)
########################################################
print("DZ6.7")
import random
s5 = set()
for i in range(10):
  s5.add(random.randint(0, 10))
s6 = set()
for i in range(10):
  s6.add(random.randint(0, 10))
print(s5, s6)
result2 = s5 - (s5 & s6)
print("result")
print(result2)
########################################################
print("DZ6.8")
import random
my_list8_1 = [(random.randint(0, 100)) for i in range(10)]
my_list8_2 = [(random.randint(0, 100)) for i in range(10)]
result_list = []
print(my_list8_1, my_list8_2)
for i in my_list8_1:
    if i not in result_list:
        result_list.append(i)
for i in my_list8_2:
    if i not in result_list:
        result_list.append(i)
print(result_list)

#  проверка на Union
s8_1 = set(my_list8_1)
s8_2 = set(my_list8_2)
result8 = s8_1.union(s8_2)
print("result")
print(result8)
########################################################
print("DZ6.9")
my_list9_1 = [(random.randint(0, 10)) for i in range(10)]
my_list9_2 = [(random.randint(0, 10)) for i in range(10)]
result_list9 = []
print(my_list9_1, my_list9_2)
for i in my_list9_1:
    if i not in my_list9_2:
        result_list9.append(i)
for j in my_list9_2:
    if j not in my_list9_1:
        result_list9.append(j)
print("result")
print(result_list9)

#  проверка на difference()

s9_1 = set(my_list9_1)
s9_2 = set(my_list9_2)
print("result")
print(s9_1.difference(s9_2))
