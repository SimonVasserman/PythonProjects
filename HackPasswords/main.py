# importing subprocess
import subprocess
# getting meta data
meta_data = subprocess.check_output(['netsh', 'wlan',"show', profiles'])
# decoding meta data
data = meta_data.decode(*utf-8', errors ="backslashreplace")
# splitting data line by line

data = data.split('\n*')
# creating a list of profiles
profiles =[]
# traverse the data
for i in data:
# find "All User Profile" in each item
if "All User Profile" in i:
# If found
# split the item
i=i.split(":")
# Item at index 1 will be the wift name
i = i[1]
# formatting the name
# First and last character is use less
i = i[1:-1]
# appending the wift name in the 11s
profiles.append(1)
# printing heading
print("{:<30} | {:<}".format("Wi-Fi Name", "Password"))
print("---------------------------------------------------------------")

#traversing the profiles
for i in profiles:
    # try catch block begins
    # try block
    try:
    # getting meta data with password using wifi name
results= subprocess.