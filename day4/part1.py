#!/usr/bin/env python3
"""
Advent of Code 2024
--- Day 4: Ceres Search  ---
Part One

Author: NC Jones
Github: ndyjones
"""

# Puzzle Instructions (aka Do I understand what I'm trying to do?)
# Word Search: For a X by Y matrix of letters find all instances of 'XMAS' 
# Word can appear horz, vert, diag, backward, overlapping
# Find all instances of the word and return count


# read the input.txt and determine the matrix dimensions
with open('input.txt', 'r') as file:
    matrix = [line.strip() for line in file]

# matrix = [
#     "XMAS",
#     "SAMX",
#     "AMAS",
#     "XMXS"
# ]

# for all lines read each line get len()
# return rows and cols, error check for len match
num_rows = len(matrix)
num_cols = len(matrix[0])

# validate dimension step
# don't assume the input is perfect
assert all(len(row) == num_cols for row in matrix), "Matrix rows have inconsistent lengths"

# visualize the matrix
# iterate over each cell in matrix

# list object for all directions horz & vert rt, lf, up, down, diag

VECTORS = [
    (0, 1), (0, -1),  # horiz right, horiz left
    (-1, 0), (1, 0),  # vert up, vert down
    (1, 1), (1, -1),  # diag down right, diag down left
    (-1, 1), (-1, -1)  # diag up right, diag up left
]

# target index (x,y) and search step thru
# xloc, yloc = 

# check for word aka 'XMAS'
word = "XMAS"
# debug check for word = 'SAMX' ## This gave the same good result on input matrix :)

def find_word(matrix, row, col, word, direction):
	num_rows, num_cols = len(matrix), len(matrix[0])
	xloc, yloc = direction # recieving the direction tuple from VECTORS

# for each char [i] in word look for valid adjacent char
	for i in range(len(word)): 
		next_row, next_col = row + i * yloc, col + i * xloc # calculate adjacent direction indices
		if not (0 <= next_row < num_rows and 0 <= next_col < num_cols):
			return False # out of bounds
		if matrix[next_row][next_col] != word[i]: # if no match gtfo
			return False # no match
	return True # good match found


# increm counter for each valid instance of word 
count = 0

# search the input matrix for the word

for row in range(num_rows):
	for col in range(num_cols):
		if matrix[row][col] == word[0]: # start with the first letter of word
			for direction in VECTORS: # use the VECTORS to loop all directions
				if find_word(matrix, row, col, word, direction): #
					count += 1


# holder for coordinates of complete 'XMAS' word

# output total count
print("Total instances of ", word, ":", count)