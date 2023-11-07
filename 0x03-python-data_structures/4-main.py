#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print("Valid index")
print(new_list)
print(my_list)

idx = -1
new_element = 19
new_list = new_in_list(my_list, idx, new_element)

print("Negative index")
print(new_list)
print(my_list)

idx = 4
new_element = 29
new_list = new_in_list(my_list, idx, new_element)

print("Last index")
print(new_list)
print(my_list)

idx = 5
new_element = 39
new_list = new_in_list(my_list, idx, new_element)

print("Last index + 1")
print(new_list)
print(my_list)

idx = 10
new_element = 49
new_list = new_in_list(my_list, idx, new_element)

print("Way out of range")
print(new_list)
print(my_list)
