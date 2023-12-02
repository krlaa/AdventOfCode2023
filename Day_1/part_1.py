# Advent of Code Day 1 Part 1

"""
input:
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

output:
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
"""

import re


# test_list:list = re.findall(pattern="(\d)",string="eight9fhstbssrplmdlncmmqqnklb39ninejz")
# print(int(f"{test_list[0]}{test_list[-1]}"))

input_file = open("input.txt")

list_of_inputs:list = input_file.readlines()

input_int = 0
for input in list_of_inputs:
    match_list:list = re.findall(pattern="(\d)",string=input)
    input_int += int(f"{match_list[0]}{match_list[-1]}")

print(input_int) 