#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print("Valid index")
print(new_list)
print(my_list)

idx = -1
new_element = 19
new_list = replace_in_list(my_list, idx, new_element)

print("Negative index")
print(new_list)
print(my_list)


idx = 10
new_element = 29
new_list = replace_in_list(my_list, idx, new_element)

print("Out of range index")
print(new_list)
print(my_list)

idx = 4
new_element = 39
new_list = replace_in_list(my_list, idx, new_element)

print("Last index")
print(new_list)
print(my_list)

idx = 5
new_element = 49
new_list = replace_in_list(my_list, idx, new_element)

print("One greater than last index")
print(new_list)
print(my_list)
