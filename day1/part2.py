#!/usr/bin/env python3
"""
Advent of Code 2024
--- Day 1: Historian Hysteria ---
Part Two

Author: NC Jones
Github: ndyjones
"""

# Puzzle Instructions (aka Do I understand what I'm trying to do?)
# Open the input file and read it's contents
# Duplicate location IDs appear in both lists
# figure out how often each left_list location ID appears in right_list, store in counter var
# calculate a total similarity score by += number in the left_list * count of times in right_list

with open('input.txt', 'r') as file:
    data = file.readlines()

left_list = []
right_list = []

# parse the input into rt and lf lists
for line in data:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

# Print the original lists
#print("Left list:", left_list)
#print("Right list:", right_list)


# Original plan: a loop to slice each number from left_list and compare to all values in right_list
# have a counter variable increment every time left value == right_list value
# increase a similarity score by the left value * total counter variable
# sum the similarity score for all values in the left list for a total similarity score

# INSTEAD don't do nested loops, be faster + scale + more pythonic, use collections.Counter dictionary
from collections import Counter

# step 1: count occurence in right_list
right_counts = Counter(right_list)

# Print the Counter object to check counts
print("Right list counts:", right_counts)

# step 2: calculate the similarity score
similarity_score = 0

#Debug for number in left_list
#    count = right_counts.get(number, 0)
#    print(f"Processing {number}: Count in right list = {count}, Contribution = {number * count}")
#    similarity_score += number * count

for number in left_list:
    similarity_score += number * right_counts.get(number, 0)

# print total similarity score
print("Total similarity score:", similarity_score)