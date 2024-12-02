#!/usr/bin/env python3
"""
Advent of Code 2024
--- Day 2: Red-Nosed Reports ---
Part Twooooooo

Author: NC Jones
Github: ndyjones
"""

# Puzzle Instructions (aka Do I understand what I'm trying to do?)
# Now create an 'problem dampener' exception condition to count toward total safe reports for each report 
# where a single increasing or decreasing value trend exceeds the range limit.

with open('input.txt', 'r') as file:
    reports = [list(map(int, line.split())) for line in file]

# safe report counter
safe_count = 0

# function to check if a report is safe
def is_safe(report):
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    return all(1 <= diff <= 3 for diff in differences) or all(-3 <= diff <= -1 for diff in differences)

# Step 3: Check each report
for report in reports:
    if is_safe(report):
        safe_count += 1
    else:
        # Try removing each level and check if the remaining report is safe
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if is_safe(modified_report):
                safe_count += 1
                break  # Stop checking once we find a way to make it safe

# output the safe count
print("Number of safe reports with Problem dampener:", safe_count)