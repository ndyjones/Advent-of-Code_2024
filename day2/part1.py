#!/usr/bin/env python3
"""
Advent of Code 2024
--- Day 2: Red-Nosed Reports ---
Part One

Author: NC Jones
Github: ndyjones
"""

# Puzzle Instructions (aka Do I understand what I'm trying to do?)
# Evaluate each report (line within the input set) and determine if the values (or levels) are increasing or decreasing gradually. 
# Verify if all differences are in the abs range [1, 3].
# If so, then that report is valid, or safe. Then that should increment a count for the total 'safe' records.

# step 1: read input data
with open('input.txt', 'r') as file:
    reports = [list(map(int, line.split())) for line in file]

# step 2: safe report counter
safe_count = 0

# step 3: Loop to evaluate each report for a increase or decrease trend
for report in reports:
    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]
    
    # Check if all differences are within [1, 3] or [-1, -3]
    if all(1 <= diff <= 3 for diff in differences) or all(-3 <= diff <= -1 for diff in differences):
        safe_count += 1

# Step 4: Output the safe count
print("Number of safe reports:", safe_count)