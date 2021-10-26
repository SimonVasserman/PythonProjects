print("DZ 4.1")
my_list = [87, 101, 103]
for value_1 in my_list:
  if value_1 > 100:
      print(value_1)
############################################################
print("DZ 4.2")
my_list_2 = [10, 65,  87, 99,  101, 53, 205, 100, 120, 103]
my_results = []
for value in my_list_2:
    if value > 100 in my_list_2:
        my_results.append(value)
print(my_results)
###############################################################
print("DZ 4.3")
my_list = [87, 101, 103]
my_list.append(my_list[-1] + my_list[-2]) if len(my_list) > 2 else my_list.append(0)
print(my_list)
###############################################################
print("DZ 4.4")
my_string = '0123456789'
my_list_4 = []
for symbol_1 in my_string:
 for symbol_2 in my_string:
   my_list_4.append(int(symbol_1 + symbol_2))
print(my_list_4)
