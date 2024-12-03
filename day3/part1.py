#!/usr/bin/env python3
"""
Advent of Code 2024
--- Day 3: Mull It Over  ---
Part One

Author: NC Jones
Github: ndyjones
"""

# Puzzle Instructions (aka Do I understand what I'm trying to do?)
# Instructions to multiply some numbers are jumbled with invalid characters
# mul(X,Y) is correct sequence for mul operation, X and Y numeric w/ values 0-999
# mul(4*, mul(6,9! and ?(13,34) or mul ( 2 , 4 ) do nothing
# for all valid instructions, multiply and sum the results
# whats the sum of all valid instructions?

# gonna need reg expressions

import re

# open input

with open('input.txt', 'r') as file:
    instructions = file.read() #read as single string
 
# define regex pattern for valid instructions
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# scan for valid instruction strings, valid = "mul(X,Y)" no spaces
valid_instructions = re.findall(pattern, instructions)

print("Number of valid instructions:", len(valid_instructions))
# print("Valid instructions captured:", valid_instructions)

# holder that appends each valid instruction on new line?
sum_of_all = 0

#then do the instructions aka X * Y
for x,y in valid_instructions:
    sum_of_all += int(x) * int(y) #make them fools integers
#    valid_instructions.append(something)

# output
print("Sum of all valid mul(X,Y) instructions:", sum_of_all)
