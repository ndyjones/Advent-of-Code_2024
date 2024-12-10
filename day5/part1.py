#!/usr/bin/env python3
"""
Advent of Code 2024
--- Day 5: Print Queue  ---
Part One

Author: NC Jones
Github: ndyjones
"""

# Puzzle Instructions (aka Do I understand what I'm trying to do?)
# Doc pages have to be printed in specific order
# For notation X|Y produced in update, page X must print before Y
# Given X|Y ordering rules and pages in update aka puzzle input, 
# determine if each update in the right order
# Also find the MIDDLE page number
# Answer =  What do you get if you add up the middle page number from those correctly-ordered updates?

# parse input.txt
with open('input.txt', 'r') as file:
	lines = file.readlines()

# split rules X|Y and comma seperated page updates
# store rules as tuples (X, Y) and pg_updates as list of ints
rules = []
pg_updates = []
parsing_rules = True

for line in lines:
	line = line.strip()
	if line == "": # blank line seperated rules and pg_updates
		parsing_rules = False
		continue
	if parsing_rules:
		x, y = map(int, line.split('|')) # parse rule X|Y tuple
		rules.append((x, y))
	else:
		pg_updates.append(list(map(int, line.split(',')))) # else parse into a pg_update

# debug input parse
# print("Rules:", rules)
# print("------------------------------")
# print("Page updates:", pg_updates)

# validate sequence against order rules
def is_valid_update(pg_update, rules):
    for x, y in rules:
        # check if both X and Y appear in the update
        if x in pg_update and y in pg_update:
            # check if X[i] is less than Y[i]
            if pg_update.index(x) >= pg_update.index(y): 
                return False  # rule violated
    return True  # all rules satisfied

# for each if both X and Y are present, ensure X comes before Y
# identify the updates already in correct order

# initialize the total sum of middle pages
total_middle = 0

# loop through all page updates
for pg_update in pg_updates:
    # check if the update is valid
    if is_valid_update(pg_update, rules):
        # find the middle page num
        middle_index = len(pg_update) // 2  # middle index
        middle_page = pg_update[middle_index]
        
        # add the middle page to the total
        total_middle += middle_page

# Output the total sum
print("Sum of middle pages:", total_middle)
