# Advent of Code Day 1 Part 2
"""
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
"""

import re

numbers_but_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# test_list:list = re.findall(pattern="(?=(one|two|three|four|five|six|seven|eight|nine|\d))",string="oneight")

# first_digit = test_list[0]
# last_digit = test_list[-1]

# if not(first_digit.isnumeric()):
#     first_digit = numbers_but_words.index(first_digit)+1
# if not(last_digit.isnumeric()):
#     last_digit = numbers_but_words.index(last_digit)+1
# print(int(f"{first_digit}{last_digit}"))



input_file = open("input.txt")

list_of_inputs:list = input_file.readlines()

input_int = 0
for input in list_of_inputs:
    match_list:list = re.findall(pattern="(?=(one|two|three|four|five|six|seven|eight|nine|\d))",string=input)
    first_digit = match_list[0]
    last_digit = match_list[-1]
    # print(f"{first_digit}{last_digit}")
    if not(first_digit.isnumeric()):
        first_digit = numbers_but_words.index(first_digit)+1
    if not(last_digit.isnumeric()):
        last_digit = numbers_but_words.index(last_digit)+1
    input_int+=int(f"{first_digit}{last_digit}")

print(input_int)
