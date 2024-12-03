#!/usr/bin/env python3
"""
Advent of Code 2024
--- Day 3: Mull It Over  ---
Part 2

Author: NC Jones
Github: ndyjones
"""

# Puzzle Instructions (aka Do I understand what I'm trying to do?)
# Instructions to multiply some numbers are jumbled with invalid characters
# mul(X,Y) is correct sequence for mul operation, X and Y numeric w/ values 0-999
# mul(4*, mul(6,9! and ?(13,34) or mul ( 2 , 4 ) do nothing
# for all valid instructions, multiply and sum the results
# PART 2 NOW do() enables future mul() instructions
# don't() disables future mul() instructions
# only the most recent do() or don't() applies, all enabled to start

# gonna need reg expressions

import re

# open input and preprocess for line breaks in input.txt

with open('input.txt', 'r') as file:
    raw_data = file.read() #read as single string
#    raw_data = file.read().replace("\n", "") # remove all line breaks
# there are no line breaks in the input file, I am dumb
 
# define regex pattern for instructions and DO and DON'T
instruction_pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
# define regex pattern for valid mul(X,Y) instructions
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# extract all valid instruction strings, valid = "mul(X,Y)" no spaces
instructions = re.findall(instruction_pattern, raw_data)

# start with active state
mul_enabled = True
sum_of_all = 0 

# for loop to process do()s and don't()s toggle
for instruction in instructions:
    if instruction == "do()":
        mul_enabled = True
    elif instruction == "don't()":
        mul_enabled = False
    else:
        # Process valid mul(X,Y) instructions if toggle enabled
        if mul_enabled:
            match = re.match(mul_pattern, instruction)
            if match:
                x, y = map(int, match.groups())
                # print(f"Processing mul: {x} * {y} = {x * y}") 
                sum_of_all += x * y #then do the instructions aka X * Y and sum
        # print("Extracted instructions:", instructions)

# print("Number of valid instructions:", len(valid_instructions))
# print("Valid instructions captured:", valid_instructions)

# output
print("Sum of all valid mul(X,Y) instructions:", sum_of_all)