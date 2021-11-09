######################################################
# DZ9.1

def buble_sort(l):
    t = l.copy()
    for n in range(0, len(t)):
        for i in range(len(t) - 1):  # вместо "n" "-1"
            if t[i] > t[n]:
                t[i], t[n] = t[n], t[i]
    return t


nums = [4, 1, 6, 3, 2, 7, 8]
sorted_list = buble_sort(nums)  # сменил название "sorted" на "sorted_list" так как sorted в python функция
print(sorted_list)

print(buble_sort([1, 3, 4, 2, 6, 7, 9, 5, 8]))
print(buble_sort([21, 13, 34, 54, 32, 17, 10, 5, 3]))
print(buble_sort([9, 2, 5, 1, 4, 7, 3, 6, 8]))
print(buble_sort([5, 2, 7, 9, 10, 4, 12, 14, 11]))
print(buble_sort([2, 1, 5, 3, 8, 4, 9, 7, 10]))
######################################################
# DZ9.2
my_list = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]


def need_list(my_list, n):
    my_result = []
    for i in my_list:
        for elem in range(len(i)):
            if elem == n:
                my_result.append(i[elem])
    return my_result


number_order = need_list(my_list, 0)
sum_order = list(map(lambda x, y: (x * y if x * y > 100 else (x + 10) * y), need_list(my_list, 2),
                     need_list(my_list, 3)))
result_order = []
for i in range(len(number_order)):
    new_list = [number_order[i], sum_order[i]]
    result_order.append(tuple(new_list))
print(result_order)

# DZ9.3

my_list2 = [
    [24387, ' на русском', 2, 4.59],
    [18762, 'The C Programming Language (2nd Edition)', 12, 78.80],
    [87236, "C Programming Absolute Beginner's Guide", 1, 23.55],
    [58132, 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14', 9, 42.89]
]

my_list.extend(my_list2)  # .extend расширяет первый список вторым списком,
# то  есть в конец перого списка добавляется второй список
print(my_list)
# DZ9.4

sorted_list_price = sorted(my_list, key=lambda x: x[3], reverse=True)
print(sorted_list_price)

# DZ9.5
sorted_list_quantity = list(filter(lambda x: x[2] > 5, my_list))
print(sorted_list_quantity)




