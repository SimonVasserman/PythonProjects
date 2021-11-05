
def exaple_read():
# sample_file = open("numbers.txt")
# data = sample_file.read()
print(data)
ret = []
for line in sample_file:
    ret.append(int(line))

print(ret)

###################################
def exaple_read():
l = [1, 21, 30, 50]
sample_file = open("numbers.txt", 'w')
for item in l:
    sample_file.write(str(item)+ "\n")\

sample_file.close()
####################################

def count_lines_old(file_name):
    sample_file = open(file_name,'r')
    l_count = 0
    for _ in sample_file:
        l_count += 1
        sample_file.close()
        return l_count

l_count = count_lines_old("numbers.txt")
print(l_count)
########################################## with ___ as

def count_lines(file_name):
  with  open(file_name,'r') as sample_file:
     l_count = 0
    for _ in sample_file:
        l_count += 1

  return l_count
###################################
  with  open(file_name,'r') as sample_file:
     i_count = 0
    for i in sample_file:
       i_count += 1
     return i_count
print(sample_file.read())


with  open(file_name,'a') as sample_file:
    sample_file.write("\ni_count")

with  open(file_name,'r') as sample_file:
    print(sample_file.read())


###############################################

def sum(list):
    assert len(list) != 0, "List should be empty"
    count = 0
    for i in list:
        count += 1
        return
