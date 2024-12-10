#!/usr/bin/env python3
"""
Advent of Code 2024
--- Day 7: Bridge Repair  ---
Part One

Author: NC Jones
Github: ndyjones
"""

# Puzzle Instructions (aka Do I understand what I'm trying to do?)
# Given a set of numbers (ex. 190: 10 19...) the 999: is a test_value that may be produced by the trailing equation values
# Determine if any combination of mathematical operators and the eq_values can produce the test_value
# operators are always evaluated left-to-right, numbers in eq_values can't be rearranged, and they are space-seperated
# add(+) and multiply(*) are the only possible operators (in this puzzle) to go between eq_values to produce test_value
# Find the total calibration result, a sum of the test_value from valid equations in the input

# parse input
with open('input.txt', 'r') as file:
    lines = file.readlines() #input 

def evaluate_recursively(values, index, current_result, test_value):
    """
    Recursively evaluate all combinations of + and * operators left-to-right.
    """
    # Base case: If we’ve reached the end of the values list
    if index == len(values):
        return current_result == test_value

    # try both + and *
    next_value = values[index]
    # add the next value
    if evaluate_recursively(values, index + 1, current_result + next_value, test_value):
        return True
    # multiply the next value
    if evaluate_recursively(values, index + 1, current_result * next_value, test_value):
        return True
    
    return False  # no valid combination found

total_valid_test = 0


for line in lines:
    # split into test value and equation values
    test_value_str, eq_values_str = line.split(":")
    test_value = int(test_value_str.strip()) # assign the first number in the line up to ':' to test_value, make it an int
    eq_values = list(map(int, eq_values_str.strip().split())) # for the numbers trailing ':' and space-seperated capture in eq_values and convert to ints

    # start recursion with the first value as the initial result
    if evaluate_recursively(eq_values, 1, eq_values[0], test_value):
        total_valid_test += test_value

# loop to determine if any combination of + and * between the eq_values can produce the test_value
# if the test_value and eq_values are valid, capture the test_value and add the next valid test_value
# if not valid eq_values, move to the next test_value and eq_value and evaluate

# Output the total sum of valid test values
print("Calibration result:", total_valid_test)