# DZ8.3
def sum_digits(n):
    if n > 0:
        return sum_digits(n // 10) + n % 10
    else:
        return 0


print(sum_digits(5))

print(10 == sum_digits(10))
print(5 == sum_digits(5))
print(4 == sum_digits(4))
print(11 == sum_digits(11))
print(1 == sum_digits(1))


#########################################
# DZ8.4
def fib(n, c=0, p=1):
    if n == 0:
        return c
    else:
        return fib(n - 1, c + p, c)


print(fib(7))

print(13 == fib(7))
print(5 == fib(5))
print(4 == fib(4))
print(11 == fib(11))
print(1 == fib(1))

##########################################
# DZ8.5
my_list = [2, 6, 5, 9, 12]


def multiply_list(list):
    if len(list) == 0:
        return 1
    else:
        return multiply_list(list[:-1]) * list[-1]


print(multiply_list(my_list))

print(6480 == multiply_list(my_list))
print(24 == multiply_list([4, 3, 2, 1]))
print(3 == multiply_list([1, 2]))
print(-5 == multiply_list([1, -5, 1]))
print(1 == multiply_list([1, 0, 0, 0]))

##########################################
# DZ8.6

n = int(input())
i = 1
while i < n:
    i = i * 2
if i == n:
    print("YES")
else:
    print("NO")


##########################################
# DZ8.7

def outer(a, b):
    def inner(a, b):
        return a + b

    return inner(a, b) + 5


print(outer(3, 2))

print(20 == outer(10, 5))
print(28 == outer(14, 5))
print(13 == outer(2, 5))
print(7 == outer(2, 0))
print(5 == outer(-5, -10))