#!/usr/bin/env python3
"""
Advent of Code 2024
--- Day 1: Historian Hysteria  ---
Part One

Author: NC Jones
Github: ndyjones
"""

# Puzzle Instructions (aka Do I understand what I'm trying to do?)
# Given an input file with two space seperated column list of numbers
# pair up smallest number in the left list with smallest number in right list
# then the second smallest left number with second smallest right number

# within each pair find out how far apart the two numbers are
# and add up all those distances for a total distance

# loop to sort two columns from input file
# extract pairs, find difference
# sum all the pair differences
# return total distance sum


# Open the input file and read it's contents

with open('input.txt', 'r') as file:
    data = file.readlines()

# create individual lists

left_list = []
right_list = []


# parse the input into rt and lf lists

for line in data:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)


# Sort both lists

left_list.sort()
right_list.sort()

total_distance = 0

# calculate the distances and sum them up
for left, right in zip(left_list, right_list):
    total_distance += abs(left - right)

print("Total distance:", total_distance)