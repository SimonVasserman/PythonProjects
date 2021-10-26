print("DZ5.1")
my_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
my_list2 = []
for i in my_list:
    if not i in my_list2:
        my_list2.append(i)
print(my_list2)
##################################################
print("DZ5.2")
my_list_2 = [10, 20, 44,  67, 87]
my_new_list = []
for i in my_list_2:
    my_new_list.append(i)
print(my_new_list)
####################################################
print("DZ5.3")
my_list_31 = [34, 56, 76, 78, 90, 99, 106, 173, 196]
my_list_32 = [34, 56, 76, 78, 90, 99]
my_list_33 = []
for i in my_list_31:
    if i not in my_list_32:
        my_list_33.append(i)
print(my_list_33)
####################################################
print("DZ5.4")
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {**dic1, **dic2, **dic3}
print(result)
####################################################
print("DZ5.5")
d = {}
for i in range(1, 16):
    key = i
    value = i ** 2
    d[key] = value
print(d)
####################################################
