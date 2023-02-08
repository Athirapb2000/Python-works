"""
1. Write a python program to generate a random color hex,
2. a random alphabetical string, random value between two integers,
3. random multiple of 7 btw 0 and 70
"""


import random

# 1
rand = random.randint(0, 16777215)
hex_num = str(hex(rand))
hex_num = '#' + hex_num[2:]
print(hex_num)

# 2