#!/usr/bin/python3
import dis
import math
magic = __import__('103-magic_class').MagicClass

dis.dis(magic)

circle = magic(6)
print(circle.area())
print(circle.circumference())
