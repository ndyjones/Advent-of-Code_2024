#!/usr/bin/env python3
"""
Advent of Code 2024
--- Day 4: Ceres Search  ---
Part Two

Author: NC Jones
Github: ndyjones
"""

# Puzzle Instructions (aka Do I understand what I'm trying to do?)
# Word Search: For a X by Y matrix of letters now looking for the specific "X" shape of 'MAS' occurences
# 'MAS' can appear diag, forward, backward, overlapping
# 'A' will always be center, 'S' and 'M' in diags no exceptions
# Find all instances of the word and return count


# read the input.txt and determine the matrix dimensions
with open('input.txt', 'r') as file:
    matrix = [line.strip() for line in file]

# validate matrix dimensions
num_rows = len(matrix)
num_cols = len(matrix[0])

# don't assume the input is perfect
assert all(len(row) == num_cols for row in matrix), "Matrix rows have inconsistent lengths"

# increm counter for each valid instance of word 
count = 0


# check for an X 'MAS' pattern
def is_xmas(matrix, row, col):
    num_rows, num_cols = len(matrix), len(matrix[0])

    # don't waste time on the edges, aka bounds
    if not (1 <= row < num_rows - 1 and 1 <= col < num_cols - 1):
        return False

    # validate diagonals
    diag1 = {matrix[row - 1][col - 1], matrix[row + 1][col + 1]}
    diag2 = {matrix[row - 1][col + 1], matrix[row + 1][col - 1]}

    if "M" in diag1 and "S" in diag1 and "M" in diag2 and "S" in diag2:
        return True

# is_xmas func is only called for valid A centers
for row in range(1, num_rows - 1):
    for col in range(1, num_cols - 1):
        if matrix[row][col] == "A" and is_xmas(matrix, row, col):
            count += 1




#### I started by trying to replicate my 'word' check loop from part 1, as a matrix, which was crazy and a hot mess
#### And full disclosure: I was getting a too low count because I think overlaps and edge cases weren't getting counted
#### had to resort to AI to walk me through, I get where the change on the edge cases tweaked added a little flexibility
#### but I don't get why overlaps were getting mismanaged. In any case here's what the AI threw out:

# # iterate through valid centers
# for i in range(1, num_rows - 1):  # avoid edges
#     for j in range(1, num_cols - 1):  # avoid edges
#         if matrix[i][j] == "A":  # center must be 'A'
#             # check diagonals
#             top_left = matrix[i - 1][j - 1]
#             top_right = matrix[i - 1][j + 1]
#             bottom_left = matrix[i + 1][j - 1]
#             bottom_right = matrix[i + 1][j + 1]

#             # validate diagonals
#             diag1 = {top_left, bottom_right}  # top left to bottom right
#             diag2 = {top_right, bottom_left}  # top right to bottom left

#             if "M" in diag1 and "S" in diag1 and "M" in diag2 and "S" in diag2:
#                 count += 1

# output total count
print("Total instances of X-MAS:", count)