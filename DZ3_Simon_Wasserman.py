value = 110
new_value = value // 2 if value > 100 else -value
print(new_value)
#####################################################
value= 90
new_value = 1 if value < 100 else 0
print(new_value)
#####################################################
value= 99
new_value = True if value < 100 else False
print(new_value)
#####################################################
my_str_1 = "homework"
result_str = my_str_1.upper()
print(result_str)
#####################################################
my_str_2 = "I AM STUDENT "
result_str_2 = my_str_2.lower()
print(result_str_2)
#####################################################
my_str_3 = "facebook"
my_str_len = len(my_str_3)
result_str_3 = my_str_3 * 2 if my_str_len < 5 else my_str_3
print(result_str_3)
#####################################################
my_str_4 = "good"
my_str_len = len(my_str_4)
result_str_4 = my_str_4 + my_str_4[::-1] if my_str_len < 5 else my_str_4
print(result_str_4)
#####################################################
