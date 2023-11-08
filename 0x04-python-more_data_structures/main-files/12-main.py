#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XXXIII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CXLVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CCCLXV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XCIV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CCLXXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
