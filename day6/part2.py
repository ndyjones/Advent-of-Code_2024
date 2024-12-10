#!/usr/bin/env python3
"""
Advent of Code 2024
--- Day 6: Guard Gallivant  ---
Part Two

Author: NC Jones
Github: ndyjones
"""

# Puzzle Instructions (aka Do I understand what I'm trying to do?)
# 2D matrix with a 'guard' faces '<,^,>,v' and moves to open space indicated by '.' obstacles indicated by "#"
# Read the grid and determine guard's starting position (row, col) and direction (facing)
# guard moves follow same rules as Part 1: 
# move one step forward in the current direction, if there is an obstacle in front, turn right 90 degrees
# Continue to simulate guard movement and test obstruction to check for guard stuck in a loop (simulate helper func)
# if the guard revisits a position with the same direction, mark the obstruction position as a valid position (test obstruction)
# count valid positions and output


## GPT help in the time and space loop complexity 
# For each grid cell, you are performing a full simulation of guard movement, which can touch every cell in the grid.
# Complexity Analysis
# Time Complexity:
#   O(N * M * T), where N and M are grid dimensions and T is the time taken to simulate the guard's movement for one test obstruction.
# Space Complexity:
#   Space is driven primarily by tracking visited positions and the grid itself, resulting in O(N * M)
# If further optimization is needed, you could explore pruning the simulation or using more advanced graph algorithms.


# parse input matrix
with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file]

# find the guard's starting position and direction
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # UP, RIGHT, DOWN, LEFT
direction_map = {"^": 0, ">": 1, "v": 2, "<": 3}  # valid direction symbols

rows, cols = len(grid), len(grid[0])
guard_row, guard_col, facing = None, None, None

for r in range(rows):
    for c in range(cols):
        if grid[r][c] in direction_map:
            guard_row, guard_col = r, c  # guard's starting position
            facing = direction_map[grid[r][c]]  # guard's starting direction
            grid[r][c] = "."  # clear the starting position

# helper function to simulate the guard's movement
def simulate_movement(grid, start_row, start_col, start_facing):
    visited = set() # holder for visited positions, directions
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # UP, RIGHT, DOWN, LEFT
    row, col, facing = start_row, start_col, start_facing

    while True:
        # detect loop: revisiting the same position with same direction
        if (row, col, facing) in visited:
            return True  # loop detected
        visited.add((row, col, facing))

        # calc the next position
        dr, dc = directions[facing]
        next_row, next_col = row + dr, col + dc

        # bounds check if the next position is out of bounds
        if not (0 <= next_row < rows and 0 <= next_col < cols):
            return False  # guard leaves the grid, no loop detected

        # check if the next position is an obstacle
        if grid[next_row][next_col] == "#":
            facing = (facing + 1) % 4  # turn right 90 degrees
        else:
            row, col = next_row, next_col  # move forward

# initialize counter for valid obstruction positions
valid_obstruction_positions = 0

# test each empty position as a potential obstruction
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "." and (r, c) != (guard_row, guard_col):  # test only empty positions
            grid[r][c] = "#"  # temporarily place an obstruction

            # simulate the guard's movement with the new obstruction
            if simulate_movement(grid, guard_row, guard_col, facing):
                valid_obstruction_positions += 1  # count valid positions

            grid[r][c] = "."  # remove the obstruction

# output the total number of valid positions
print("Valid obstruction positions:", valid_obstruction_positions)