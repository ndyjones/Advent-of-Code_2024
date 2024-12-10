#!/usr/bin/env python3
"""
Advent of Code 2024
--- Day 6: Guard Gallivant  ---
Part One

Author: NC Jones
Github: ndyjones
"""

# Puzzle Instructions (aka Do I understand what I'm trying to do?)
# 2D matrix with a 'guard' faces '<,^,>,v' and moves to open space indicated by '.' obstacles indicated by "#"
# Read the grid and determine guard's starting position (row, col) and direction (facing)
# guard moves follow rules to move forward if there is no obstacle directly in front
# move one step forward in the current direction, if there is an obstacle in front, turn right 90 degrees
# Track all positions that the guard visits before leaving the mapped area

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
            guard_row, guard_col = r, c
            facing = direction_map[grid[r][c]]
            grid[r][c] = "."  # clear the starting position

# simulate the guard's movement
visited = set()
visited.add((guard_row, guard_col))  # Include the starting position

while True:
    # calc the next position
    dr, dc = directions[facing]
    next_row, next_col = guard_row + dr, guard_col + dc

    # bounds check if the next position is out of bounds
    if not (0 <= next_row < rows and 0 <= next_col < cols):
        break  # Guard leaves the grid, stop simulation

    # check if the next position is an obstacle
    if grid[next_row][next_col] == "#":
        facing = (facing + 1) % 4  # turn right 90 degrees
    else:
        # Move forward
        guard_row, guard_col = next_row, next_col
        visited.add((guard_row, guard_col))

# output result count
print("Distinct positions visited:", len(visited))
