#!/usr/bin/python3
Square1 = __import__('6-square').Square
Square2 = __import__('101-square').Square

my_square_2 = Square1(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square2(3, (1, 1))
print(my_square_3)

print("--")

my_square_2 = Square1(4, (0, 0))
my_square_2.my_print()

print("--")

my_square_3 = Square2(4, (0, 0))
print(my_square_3)

print("--")

my_square_2 = Square1(0, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square2(0, (1, 1))
print(my_square_3)

print("--")
